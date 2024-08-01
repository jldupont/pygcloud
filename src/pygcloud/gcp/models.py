"""
Data models related to GCP services

NOTE The classvar `REF_NAME` contains the string
     used to reference the service in various links
     such as 'users', 'target', "selfLink' etc.

@author: jldupont
"""

import re
from typing import List, Dict, Union, Any, ClassVar
from dataclasses import dataclass, field
from collections import UserDict
from pygcloud.utils import JsonObject
from pygcloud.models import Spec, spec


class UnknownRef(Exception):
    """
    Used to signal unknown
    or (yet) unsupported reference
    """


Str = Union[str, None]

EXCEPT_SLASH = "([^/]+)"

PROJECT = f"/projects/(?P<project>{EXCEPT_SLASH})"
REGION = f"/regions/(?P<region>{EXCEPT_SLASH})"
GLOBAL = "/(?P<region>global)"
SERVICE_TYPE_NAME = f"/(?:(?P<service_type>{EXCEPT_SLASH}))/(?P<name>{EXCEPT_SLASH})"

#
# The order is important: longest first
#
PATTERNS = [
    re.compile(PROJECT + REGION + SERVICE_TYPE_NAME),
    re.compile(PROJECT + GLOBAL + SERVICE_TYPE_NAME),
    re.compile(PROJECT + GLOBAL),
    re.compile(PROJECT + REGION),
]


@dataclass
class Ref:

    project: str
    region: str
    service_type: Str = field(default_factory=str)
    name: Str = field(default_factory=str)

    @classmethod
    def match(cls, input):

        result = None
        for pattern in PATTERNS:
            result = pattern.search(input)
            if result is not None:
                break

        if result is None:
            raise UnknownRef(repr(input))

        return result.groupdict()

    @classmethod
    def from_link(cls, link: str):
        assert isinstance(link, str)
        result = cls.match(link)
        return cls(**result)


class LinksMap(UserDict):
    """
    Holds link references found in Spec

    Once set, (key:value) mappings cannot be changed
    but LinksMap silently observes idempotency
    """

    def __setitem__(self, key, value):
        if key is None:
            return
        current = self.get(key, None)
        if current is not None:
            if current != value:
                raise ValueError(f"Link key already exists: {key}")
        super().__setitem__(key, value)

    def __delitem__(self, key: str):
        raise ValueError(f"Single key cannot be removed: {key}")


@spec
@dataclass
class ProjectDescription(Spec):
    name: str
    projectId: str
    projectNumber: str
    lifecycleState: str
    parent: dict


@spec
@dataclass
class ServiceDescription(Spec):
    """
    A service description as retrieved through
    `gcloud services list --enabled`
    """

    name: str
    state: str
    parent: str
    project_number: int = 0
    api: str = "???"

    def __post_init__(self):
        parts = self.name.split("/")
        self.project_number = parts[1]
        self.api = parts[-1]

@spec
@dataclass
class IAMBinding(Spec):
    """
    By default, if the 'email' does not
    contain a namespace prefix, it will be
    set to "serviceAccount"
    """

    email: str
    role: str
    ns: str = field(default=None)

    def __post_init__(self):
        if self.ns is not None:
            return

        maybe_split = self.email.split(":")
        if len(maybe_split) == 2:
            self.ns = maybe_split[0]
            self.email = maybe_split[1]
        else:
            self.ns = "serviceAccount"

    @property
    def sa_email(self):
        return f"{self.ns}:{self.email}"

    @property
    def member(self):
        return f"{self.ns}:{self.email}"


class _IAMMember:

    @classmethod
    def from_obj(cls, obj):

        if isinstance(obj, list):
            return [cls.from_obj(item) for item in obj]

        assert isinstance(obj, str), print(
            f"{cls.__name__}: Expecting string, got: {obj}"
        )

        parts = obj.split(":")
        ns = parts[0]
        email = parts[-1]

        return cls(ns=ns, email=email)


@spec
@dataclass
class IAMMember(_IAMMember, Spec):
    """
    NOTE in some cases, 'email' is really a name or id
         e.g. ns: projectEditor
              email: $project_id
    """

    ns: str
    email: str

    @property
    def member(self):
        return f"{self.ns}:{self.email}"


@spec
@dataclass
class IAMBindings(Spec):

    members: List[IAMMember]
    role: str


@spec
@dataclass
class IAMPolicy(Spec):

    bindings: List[IAMBindings]

    @classmethod
    def from_json_list(cls, json_str: str, path: Str = None):
        bindings = IAMBindings.from_json_list(json_str, path="bindings")
        return cls(bindings=bindings)

    from_string = from_json_list

    def contains(self, binding: IAMBinding) -> bool:
        """
        Determine if a specific binding is contained in the policy
        """
        binding: IAMBindings

        member = IAMMember(ns=binding.ns, email=binding.email)

        # scan through all bindings looking
        # for all entries pertaining to the target member
        for _binding in self.bindings:
            if member in _binding.members:
                if binding.role == _binding.role:
                    return True

        return False


@spec
@dataclass
class IPAddress(Spec):
    """
    Compute Engine IP address
    """

    REF_NAME: ClassVar[str] = "addresses"

    name: str
    address: str
    addressType: str
    ipVersion: str
    selfLink: str
    users: List[str] = field(default_factory=list)


@spec
@dataclass
class CloudRunRevisionSpec(Spec):
    """
    Cloud Run Revision Specification (flattened)
    """

    name: str
    url: str
    labels: Dict
    service_account: str

    @classmethod
    def from_obj(cls, obj):
        d = {
            "url": obj["status.url"],
            "labels": obj["spec.template.metadata.labels"],
            "name": obj["metadata.name"],
            "service_account": obj["spec.template.spec.serviceAccountName"],
        }

        return cls(**d)

    @classmethod
    def from_string(cls, json_str: str):
        obj = JsonObject.from_string(json_str)
        return cls.from_obj(obj)

    @classmethod
    def from_json_list(cls, json_list, path: str = None):
        liste: List = cls.parse_json(json_list)  # type: ignore

        entries = []
        for obj_dict in liste:
            jso = JsonObject(obj_dict)
            obj = cls.from_obj(jso)
            entries.append(obj)

        return entries


@spec
@dataclass
class BackendGroup(Spec):
    """
    group: e.g. can contain a link to a NEG
    """

    balancingMode: str
    group: str
    capacityScaler: int


@spec
@dataclass
class BackendServiceSpec(Spec):
    """
    https://cloud.google.com/compute/docs/reference/rest/v1/backendServices
    """

    name: str
    port: int
    portName: str
    protocol: str
    selfLink: str
    backends: List[BackendGroup]
    iap: Dict = field(default_factory=dict)
    usedBy: List[Any] = field(default_factory=list)


@spec
@dataclass
class FwdRule(Spec):
    """Attribute names come directly from gcloud describe"""

    REF_NAME: ClassVar[str] = "forwardingRules"

    name: str
    IPAddress: str
    IPProtocol: str
    loadBalancingScheme: str
    networkTier: str
    portRange: str
    selfLink: str
    target: str


@spec
@dataclass
class GCSBucket(Spec):
    name: str
    location: str
    default_storage_class: str
    location_type: str
    metageneration: int
    public_access_prevention: str
    uniform_bucket_level_access: str


@spec
@dataclass
class SSLCertificate(Spec):
    """
    CAUTION: sensitive information in the 'certificate' field
    """

    name: str
    type: str
    selfLink: str
    managed: dict = field(default_factory=dict)


@spec
@dataclass
class HTTPSProxy(Spec):
    """
    sslCertificates: list of links
    """

    name: str
    selfLink: str
    sslCertificates: List[str] = field(default_factory=list)
    urlMap: str = field(default_factory=str)


@spec
@dataclass
class SchedulerJob(Spec):
    name: str
    retryConfig: dict
    schedule: str
    state: str
    timeZone: str
    location: str = "???"
    pubsubTarget: dict = field(default_factory=dict)


@spec
@dataclass
class PubsubTopic(Spec):
    name: str

    def __post_init__(self):
        parts = self.name.split("/")
        self.name = parts[-1]


@spec
@dataclass
class FirestoreDb(Spec):
    name: str
    type: str
    locationId: str
    concurrencyMode: str
    pointInTimeRecoveryEnablement: str

    def __post_init__(self):
        parts = self.name.split("/")
        self.name = parts[-1]


@spec
@dataclass
class CloudRunNegSpec(Spec):

    name: str
    networkEndpointType: str
    selfLink: str
    region: str = field(default_factory=str)
    cloudRun: dict = field(default_factory=dict)


@spec
@dataclass
class TaskQueue(Spec):

    name: str
    state: str
    location: str = field(default_factory=str)
    rateLimits: dict = field(default_factory=dict)
    retryConfig: dict = field(default_factory=dict)


@spec
@dataclass
class UrlMap(Spec):
    """
    defaultService: a link to a service
    """

    selfLink: str
    id: str = field(default_factory=str)
    name: str = field(default_factory=str)
    defaultService: str = field(default_factory=str)


@spec
@dataclass
class ServiceAccountSpec(Spec):
    name: str
    email: str
    projectId: str
    uniqueId: str
    oauth2ClientId: str
    displayName: str = field(default_factory=str)
    description: str = field(default_factory=str)

    def is_default(self):
        """
        Is this service account a default one
        """
        return "iam.gserviceaccount.com" not in self.email

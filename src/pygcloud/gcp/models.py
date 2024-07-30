"""
Data models related to GCP services

@author: jldupont
"""

from typing import List, Dict, Union, Any
from dataclasses import dataclass, field
from collections import UserDict
from pygcloud.utils import JsonObject
from pygcloud.models import Spec


Str = Union[str, None]


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


@dataclass
class ProjectDescription(Spec):
    name: str
    projectId: str
    projectNumber: str
    lifecycleState: str
    parent: dict


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


@dataclass
class IAMBindings(Spec):

    members: List[IAMMember]
    role: str


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
            # print(f"> processing binding: {_binding}")

            if member in _binding.members:
                # print(f"Found member: {member}")

                if binding.role == _binding.role:
                    return True

        return False


@dataclass
class IPAddress(Spec):
    """
    Compute Engine IP address
    """

    name: str
    address: str
    addressType: str
    ipVersion: str
    selfLink: str
    users: List[str] = field(default_factory=list)


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


@dataclass
class BackendGroup(Spec):
    """
    group: e.g. can contain a link to a NEG
    """
    balancingMode: str
    group: str
    capacityScaler: int


@dataclass
class BackendServiceSpec(Spec):

    name: str
    port: int
    portName: str
    protocol: str
    selfLink: str
    backends: List[BackendGroup]
    iap: Dict = field(default_factory=dict)
    usedBy: List[Any] = field(default_factory=list)


@dataclass
class FwdRule(Spec):
    """Attribute names come directly from gcloud describe"""

    name: str
    IPAddress: str
    IPProtocol: str
    loadBalancingScheme: str
    networkTier: str
    portRange: str
    selfLink: str
    target: str


@dataclass
class GCSBucket(Spec):
    name: str
    location: str
    default_storage_class: str
    location_type: str
    metageneration: int
    public_access_prevention: str
    uniform_bucket_level_access: str


@dataclass
class SSLCertificate(Spec):
    """
    CAUTION: sensitive information in the 'certificate' field
    """

    name: str
    type: str
    selfLink: str
    managed: dict = field(default_factory=dict)


@dataclass
class HTTPSProxy(Spec):
    """
    sslCertificates: list of links
    """
    name: str
    selfLink: str
    sslCertificates: List[str] = field(default_factory=list)
    urlMap: str = field(default_factory=str)


@dataclass
class SchedulerJob(Spec):
    name: str
    retryConfig: dict
    schedule: str
    state: str
    timeZone: str
    location: str = "???"
    pubsubTarget: dict = field(default_factory=dict)


@dataclass
class PubsubTopic(Spec):
    name: str

    def __post_init__(self):
        parts = self.name.split("/")
        self.name = parts[-1]


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


@dataclass
class CloudRunNegSpec(Spec):

    name: str
    networkEndpointType: str
    selfLink: str
    region: str = field(default_factory=str)
    cloudRun: dict = field(default_factory=dict)


@dataclass
class TaskQueue(Spec):

    name: str
    state: str
    location: str = field(default_factory=str)
    rateLimits: dict = field(default_factory=dict)
    retryConfig: dict = field(default_factory=dict)


@dataclass
class UrlMap(Spec):
    """
    defaultService: a link to a service
    """

    selfLink: str
    id: str = field(default_factory=str)
    name: str = field(default_factory=str)
    defaultService: str = field(default_factory=str)


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

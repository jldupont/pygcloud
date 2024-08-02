"""
Data models related to GCP services

NOTE The classvar `REF_NAME` contains the string
     used to reference the service in various links
     such as 'users', 'target', "selfLink' etc.

@author: jldupont
"""

import re
from typing import List, Dict, Union, ClassVar
from dataclasses import dataclass, field
from collections import UserDict
from pygcloud.models import Spec, spec, GCPService


class UnknownRef(Exception):
    """
    Used to signal unknown
    or (yet) unsupported reference
    """


Str = Union[str, None]

EXCEPT_SLASH = "([^/]+)"

# CloudRun example...
# /apis/serving.knative.dev/v1/namespaces/215695389495/services/SERVICE'

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


class _Ref:
    """Private methods"""

    __all_instances__: ClassVar[List] = []

    @classmethod
    def add(cls, instance):
        assert isinstance(instance, cls), print({instance})
        cls.__all_instances__.append(instance)

    append = add
    __add__ = add

    @classmethod
    def clear(cls):
        cls.__all_instances__.clear()

    @classmethod
    @property
    def all_instances(cls):
        return cls.__all_instances__

    def __post_init__(self):
        self.add(self)

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
    def from_link(cls, link: str, origin_service: GCPService = None):
        assert isinstance(link, str), print(link)
        result = cls.match(link)
        return cls(**result, origin_service=origin_service)

    def to_json_string(self):
        import json
        from .utils import FlexJSONEncoder

        return json.dumps(self.to_dict(), cls=FlexJSONEncoder)

    def to_dict(self):
        result = {}
        fields = self.__annotations__

        for _field in fields:
            value = getattr(self, _field)

            if hasattr(value, "to_dict"):
                value = value.to_dict()

            result[_field] = value

        return result

    @classmethod
    def from_obj(cls, obj: Union[str, Dict, List], origin_service: GCPService = None):

        if isinstance(obj, List):
            return [cls.from_obj(item, origin_service=origin_service) for item in obj]

        assert isinstance(obj, (str, dict)), print(obj)

        if isinstance(obj, str):
            name = obj

        if isinstance(obj, dict):
            name = obj.get("reference", None)

        if name is None:
            raise Exception(f"Unexpected None whilst processing obj= {repr(obj)}")

        return cls.from_link(name, origin_service)

    def _vector(self):
        return f"{self.project}/{self.region}/{self.service_type}/{self.name}"

    def __repr__(self):
        return self._vector()


@dataclass
class Ref(_Ref):

    project: str
    region: str
    service_type: Str = field(default_factory=str)
    name: Str = field(default_factory=str)
    origin_service: GCPService = field(default=None)

    def __hash__(self):
        """NOTE this cannot be moved to _Ref"""
        return hash(self._vector())


@dataclass
class RefSelfLink(Ref):
    """selfLink"""

    def __hash__(self):
        """NOTE this cannot be moved to _Ref"""
        return hash(self._vector())


@dataclass
class RefUses(Ref):
    """uses"""

    def __hash__(self):
        """NOTE this cannot be moved to _Ref"""
        return hash(self._vector())


@dataclass
class RefUsedBy(Ref):
    """usedBy"""

    def __hash__(self):
        """NOTE this cannot be moved to _Ref"""
        return hash(self._vector())


class LinksMap(UserDict):
    """
    Holds link references found in Spec

    Once set, (key:value) mappings cannot be changed
    but LinksMap silently observes idempotency

    NOTE Not used at the moment
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
class UnknownSpecType(Spec):
    """
    Placeholder for unknown / unsupported spec types
    """


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
    def from_json_list(cls, json_str: str, path: Str = None, origin_service=None):
        bindings = IAMBindings.from_json_list(
            json_str, path="bindings", origin_service=origin_service
        )
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
    selfLink: RefSelfLink
    users: List[RefUses] = field(default_factory=list)


@dataclass
class CloudRunMetadata(Spec):

    name: str
    annotations: dict
    selfLink: str  # RefSelfLink


@dataclass
class CloudRunTemplateSpec(Spec):
    serviceAccountName: str = field(default=None)


@dataclass
class CloudRunTemplate(Spec):
    spec: CloudRunTemplateSpec


@dataclass
class CloudRunSpec(Spec):
    template: CloudRunTemplate = field(default=None)


@dataclass
class CloudRunStatus(Spec):
    url: str


@spec
@dataclass
class CloudRunRevisionSpec(Spec):
    """
    Cloud Run Revision Specification (flattened)

    NOTE the selfLink format:
         "/apis/serving.knative.dev/v1/namespaces/$project_number/services/$name"
    """

    spec: CloudRunSpec
    status: CloudRunStatus
    metadata: CloudRunMetadata
    name: str = field(default=None)

    def __post_init_ex__(self):
        self.name = self.metadata.name


@spec
@dataclass
class BackendGroup(Spec):
    """
    This model is contained, AFAIK, only within
    the BackendServiceSpec

    NOTE group: can contain a link ref to a NEG
    """

    balancingMode: str
    group: RefUses
    capacityScaler: int


@spec
@dataclass
class BackendServiceSpec(Spec):
    """
    https://cloud.google.com/compute/docs/reference/rest/v1/backendServices

    NOTE selfLink e.g.
    "https://www.googleapis.com/compute/v1/projects/$project
        /global/backendServices/$name",
    """

    REF_NAME: ClassVar[str] = "backendServices"

    name: str
    port: int
    portName: str
    protocol: str
    selfLink: RefSelfLink
    backends: List[BackendGroup]
    iap: Dict = field(default_factory=dict)
    usedBy: List[RefUsedBy] = field(default_factory=list)


@spec
@dataclass
class FwdRule(Spec):
    """
    NOTE selfLink e.g.
        https://www.googleapis.com/compute/v1/projects/$project
            /global/forwardingRules/$name

        target e.g.:
        https://www.googleapis.com/compute/v1/projects/$project
            /global/targetHttpsProxies/$name
    """

    REF_NAME: ClassVar[str] = "forwardingRules"

    name: str
    IPAddress: str
    IPProtocol: str
    loadBalancingScheme: str
    networkTier: str
    portRange: str
    selfLink: RefSelfLink
    target: RefUses


@spec
@dataclass
class ACL(Spec):
    entity: str
    role: str


@spec
@dataclass
class GCSBucket(Spec):
    """
    NOTE 'name' is without the leading "gs://"
    """

    name: str
    location: str
    default_storage_class: str
    location_type: str
    metageneration: int
    public_access_prevention: str
    uniform_bucket_level_access: str
    acl: List[ACL] = field(default=list)
    default_acl: List[ACL] = field(default=list)


@spec
@dataclass
class SSLCertificate(Spec):
    """
    CAUTION: sensitive information in the 'certificate' field

    NOTE selfLink e.g.
        "https://www.googleapis.com/compute/v1/projects/$project
            /global/sslCertificates/$name"
    """

    REF_NAME: ClassVar[str] = "sslCertificates"

    name: str
    type: str
    selfLink: RefSelfLink
    managed: dict = field(default_factory=dict)


@spec
@dataclass
class HTTPSProxy(Spec):
    """
    sslCertificates: list of link refs
    urlMap: link ref
    """

    REF_NAME: ClassVar[str] = "targetHttpsProxies"

    name: str
    selfLink: RefSelfLink
    sslCertificates: List[RefUses] = field(default_factory=list)
    urlMap: str = field(default_factory=str)


@spec
@dataclass
class SchedulerJob(Spec):
    """
    NOTE topicName e.g.
            "projects/$project/topics/$name"
    """

    name: str
    retryConfig: dict
    schedule: str
    state: str
    timeZone: str
    location: str = "???"
    pubsubTarget: dict = field(default_factory=dict)
    topicName_: str = field(default_factory=str)

    def __post_init_ex__(self):
        self.topicName_ = self.pubsubTarget.get("topicName", None)


@spec
@dataclass
class PubsubTopic(Spec):
    """
    NOTE name e.g.
            "projects/$project/topics/$name"
    """

    name: str

    def __post_init__(self):
        parts = self.name.split("/")
        self.name = parts[-1]


@spec
@dataclass
class FirestoreDb(Spec):
    """
    NOTE name format:
            projects/$PROJECT/databases/$db_name
    """

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
    """
    NOTE region e.g.
            https://www.googleapis.com/compute/beta/projects/$project
                /regions/$region

        selfLink e.g.:
            https://www.googleapis.com/compute/beta/projects/$project
                /regions/$region/networkEndpointGroups/$name
    """

    REF_NAME: ClassVar[str] = "networkEndpointGroups"

    name: str
    networkEndpointType: str
    selfLink: RefSelfLink
    region: str = field(default_factory=str)
    cloudRun: dict = field(default_factory=dict)


@spec
@dataclass
class TaskQueue(Spec):
    """
    NOTE name e.g.
            projects/$project/locations/$location/queues/$name
    """

    name: str
    state: str
    location: str = field(default_factory=str)
    rateLimits: dict = field(default_factory=dict)
    retryConfig: dict = field(default_factory=dict)


@spec
@dataclass
class UrlMap(Spec):
    """
    NOTE defaultService e.g.
            https://www.googleapis.com/compute/v1/projects/$project
                /global/backendServices/$name

    NOTE selfLink e.g.
            https://www.googleapis.com/compute/v1/projects/$project
                /global/urlMaps/$name
    """

    REF_NAME: ClassVar[str] = "urlMaps"

    selfLink: str
    id: str = field(default_factory=str)
    name: str = field(default_factory=str)
    defaultService: str = field(default_factory=str)


@spec
@dataclass
class ServiceAccountSpec(Spec):
    """
    "name":
        "projects/$project/serviceAccounts/
            $project_number-compute@developer.gserviceaccount.com"
    """

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

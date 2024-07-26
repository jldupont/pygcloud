"""
@author: jldupont
"""

import os
import logging
from functools import cache
from collections import UserList
from typing import List, Tuple, NewType, Union, Callable, Any
from abc import abstractmethod
from dataclasses import dataclass, field
from .constants import ServiceCategory, Instruction


class OptionalParam(UserList):
    """
    If the value resolves to None, the list resolves to empty.

    If the value resolves to something other than None,
    then the list resolves to [param, value]
    """

    def __init__(self, param, value):
        if value is None:
            super().__init__()
        else:
            super().__init__([param, value])


class OptionalParamFromAttribute(UserList):
    """
    If the value of the attribute on the obj
    resolves to "not None", return the list
    []
    """
    def __init__(self, param: str, obj: Any, attr: str):
        assert isinstance(param, str)
        assert isinstance(attr, str)

        if obj is None:
            return super().__init__()

        value = getattr(obj, attr, None)
        if value is None:
            return super().__init__()

        super().__init__([param, value])


class EnvValue(str):
    """
    Retrieve a value from an environment variable
    """

    def __new__(cls, name, default=None):
        value = os.environ.get(name, default)
        instance = super().__new__(cls, value)
        return instance


class LazyValue:
    """
    Abstract base class for lazy resolvers
    """


class LazyEnvValue(str, LazyValue):
    """
    Retrieve a value from an environment variable

    Other operators aside from __eq__ and __neq__
    might be required in the future
    """

    def __init__(self, name):
        super().__init__()
        self._name = name

    @property
    def value(self):
        v = os.environ.get(self._name, None)
        if v is None:
            raise ValueError(f"Environment var '{self._name}' does not exist")
        return v

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        v = os.environ.get(self._name, None)
        return f"LazyEnvValue({self._name}) = {v}"


class LazyAttrValue(LazyValue):
    """
    Retrieve a value from an object

    The attribute name can be nested
    using "dot" notation

    See example in the unit-test
    """

    def __init__(self, obj: Any, path: str):
        self._obj = obj
        self._path = path

    @property
    def value(self):
        try:
            parts = self._path.split(".")
            result = self._obj

            while parts:
                key = parts.pop(0)
                if isinstance(result, dict):
                    result = result[key]
                else:
                    result = getattr(result, key)

            return result
        except Exception as e:
            logging.warning(e)
            raise ValueError("Cannot resolve value")

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        obj_repr = repr(self._obj)
        return f"LazyAttrValue({obj_repr}, {self._path})"


@dataclass
class Param:
    """Description of a gcloud parameter"""

    key: str
    value: str

    def __len__(self):
        return 2

    def __getitem__(self, index):

        if index == 0:
            return self.key

        if index == 1:
            return self.value

        # unpacking tuple requires
        # iteration protocol
        raise StopIteration


class EnvParam(Param):
    """
    For parameters coming from environment variables
    """

    def __init__(self, key: str, env_var_name: str, default: Union[str, None] = None):
        """
        key: parameter name
        env_var_name: environment variable name
        """
        assert isinstance(key, str)
        assert isinstance(env_var_name, str)

        value = os.environ.get(env_var_name, default)
        if value is None:
            raise ValueError(f"Environment variable {env_var_name} not found")
        super().__init__(key, value)

    def __str__(self):
        return self.value


Params = NewType("Params", Union[List[Tuple[str, str]], List[Param]])
Label = NewType("Label", Tuple[str, str])
GroupName = NewType("GroupName", Union[str, EnvValue])


class GroupNameUtility:

    @staticmethod
    def is_of_type(what: GroupName):
        return isinstance(what, str) or isinstance(what, EnvValue)

    @staticmethod
    def resolve_group_name(name: GroupName) -> str:

        if isinstance(name, str):
            return name

        if isinstance(name, EnvValue):
            return name.value

        raise Exception(f"Expecting a valid name, got: {name}")


@dataclass(frozen=True)
class Result:
    success: bool
    message: str
    code: int


class ServiceMeta(type):

    @classmethod
    def only_add_real_service_class(cls, classe):
        new_class_name = classe.__name__.lower()

        if "mock" in new_class_name:
            return

        if new_class_name == "servicenode":
            return

        if "gcpservice" in new_class_name:
            return

        cls.__all_classes__.append(classe)

    def __new__(cls, name, bases, attrs):

        if not getattr(cls, "__all_classes__", False):
            setattr(cls, "__all_classes__", [])

        new_class = super().__new__(cls, name, bases, attrs)
        cls.only_add_real_service_class(new_class)
        return new_class


class ServiceNode(metaclass=ServiceMeta):
    """
    Protocol to establish "use" relationships
    between services
    """

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def ns(self):
        raise NotImplementedError


class GCPService(ServiceNode):
    """
    Base class for GCP services

    The 'name' and 'ns' (namespace) parameters are
    only useful when the relationship "use" feature is used.

    We do not use the class name as namespace because
    it might happen we will extend the classes to support
    more usecases.

    REQUIRES_UPDATE_AFTER_CREATE: provides support for services
    which cannot be fully configured during the creation phase.
    For example, Google GCS cannot set labels during creation.

    REQUIRES_DESCRIBE_BEFORE_CREATE: for "create only" services
    that requires checking for existence before attempting creation.
    For example: Firestore database.

    SERVICE_ACCOUNT_SUPPORTED: if the service can be deployed with its
    own service account.
    """

    SERVICE_CATEGORY: ServiceCategory = ServiceCategory.INDETERMINATE
    SERVICE_ACCOUNT_SUPPORTED = False
    REQUIRES_UPDATE_AFTER_CREATE: bool = False
    REQUIRES_DESCRIBE_BEFORE_CREATE: bool = False
    LISTING_CAPABLE: bool = False
    LISTING_REQUIRES_LOCATION: bool = False
    DEPENDS_ON_API: Union[str, None] = None
    SPEC_CLASS = None
    GROUP: List[str] = []
    GROUP_SUB_DESCRIBE: List[str] = []

    @property
    def category(self):
        return self.SERVICE_CATEGORY

    @property
    def name(self):
        return self._name

    @property
    def ns(self):
        return self._ns

    def __init__(self, name=None, ns=None):
        """
        name: string (optional)
        ns: string (optional)
        """
        self.already_exists = None  # indeterminated
        self.last_result = None
        self._name = name
        self._ns = ns
        self._uses: List[ServiceNode] = []
        self._callables_before_deploy: List[Callable] = []
        self._just_describe = False
        self._spec = None

    @property
    def spec(self):
        return self._spec

    @property
    def just_describe(self):
        return self._just_describe

    def set_just_describe(self, enable: bool = True):
        self._just_describe = enable
        return self

    def __repr__(self):
        return f"""
        {self.__class__.__name__}
        (already_exists={self.already_exists},
        last_result={self.last_result}
        )
        """.strip()

    def add_task_before_deploy(self, task: Union[Callable, List[Callable]]):

        if isinstance(task, Callable):
            self._callables_before_deploy.append(task)
            return self

        if isinstance(task, List):
            self._callables_before_deploy.extend(task)
            return self

        raise Exception("Expecting task or task list, " f"got: {type(task)}")

    @classmethod
    @cache
    def generate_label(cls, target: ServiceNode) -> str:
        """
        Needs to be implemented in a derived class
        """
        return None

    def validate_label(self, target: ServiceNode) -> bool:
        try:
            self.generate_label(target)

        except Exception:
            return False

        return True

    def before_use(self, target_service: ServiceNode):
        """
        Raises exception if a valid label cannot be derived
        """
        if self.validate_label(self) is None:
            logging.warning(
                "Label validation is not available for:" f" {self.__class__.name}"
            )
        else:
            self.validate_label(self)

        if not self.validate_label(target_service):
            logging.warning(
                "Label validation is not available for:"
                f" {target_service.__class__.name}"
            )
        else:
            self.validate_label(target_service)

    def use(self, service: ServiceNode):
        self.before_use(service)
        self._uses.append(service)
        self.after_use(service)
        return self

    def after_use(self, service: ServiceNode):
        pass

    @property
    def uses(self) -> List[ServiceNode]:
        return self._uses

    def before_deploy(self) -> Union[Instruction, None]:
        """
        Called by Deployer

        If Instruction.ABORT_DEPLOY is returned by a task,
        the Deployer will abort the deployment of the
        current service.
        """

        instruction = None
        for task in self._callables_before_deploy:

            try:
                tname = task.__name__
            except Exception:
                # partial functions do not have __name__
                tname = str(task)

            logging.debug(f"before_deploy: executing {tname}")
            instruction = task()
            if instruction is not None:
                if instruction.is_abort():
                    return instruction

        # returns last instruction ; plan accordingly
        return instruction

    def before_describe(self):
        """This is service specific"""

    def before_create(self):
        """This is service specific"""

    def before_update(self):
        """This is service specific"""

    def before_delete(self):
        """This is service specific"""

    def params_describe(self) -> Params:
        """This is service specific"""
        raise NotImplementedError

    def params_create(self) -> Params:
        """This is service specific"""
        raise NotImplementedError

    def params_update(self) -> Params:
        """This is service specific"""
        raise NotImplementedError

    def params_delete(self) -> Params:
        """This is service specific"""
        raise NotImplementedError

    def after_describe(self, result: Result) -> Result:
        """This is service specific"""
        self.last_result = result

        if not result.success:
            return result

        if result.success:
            self.already_exists = True
            if self.SPEC_CLASS is not None:
                self._spec = self.SPEC_CLASS.from_string(result.message)

        return result

    def after_create(self, result: Result) -> Result:
        self.last_result = result

        if not result.success:
            return result

        if result.success:
            self.already_exists = False
            if self.SPEC_CLASS is not None:
                self._spec = self.SPEC_CLASS.from_string(result.message)

        return result

    def after_update(self, result: Result) -> Result:
        self.last_result = result
        return result

    def after_delete(self, result: Result) -> Result:
        self.last_result = result
        return result

    def after_deploy(self):
        """Called by Deployer"""


class GCPServiceSingletonImmutable(GCPService):
    """
    Base class for GCP services that can only be created once.
    Example: Firestore indexes

    For this class, we ignore exceptions arising from the
    service already being created: we do this by interpreting
    the result code in the "after_create" method.
    """

    SERVICE_CATEGORY = ServiceCategory.SINGLETON_IMMUTABLE

    def before_create(self):

        # We do not know if the service already exists
        # but we set it to False to simplify the creation
        # of derived classes
        self.already_exists = False
        self.last_result = None

    def after_create(self, result: Result) -> Result:

        self.last_result = result

        # Case 1: the service was just created
        if result.code == 0:
            return super().after_create(result)

        # Case 2: Check if the service already exists
        lmsg = result.message.lower()

        if "already_exists" in lmsg or \
                "already exists" in lmsg:

            # fake idempotence
            self.already_exists = True
            new_result = Result(success=True, message=result.message, code=0)
            self.last_result = new_result
            return new_result

        return result


class GCPServiceRevisionBased(GCPService):
    """
    Base class for GCP services that deploy with unique revisions
    """

    SERVICE_CATEGORY = ServiceCategory.REVISION_BASED

    def before_update(self):
        raise Exception("This method should not be implemented")

    def after_update(self, result: Result) -> Result:
        raise Exception("This method should not be implemented")


class GCPServiceUpdatable(GCPService):
    """
    Base class for GCP services that can be updated
    but must be created first
    """

    SERVICE_CATEGORY = ServiceCategory.UPDATABLE


class ServiceGroup(list):
    """
    Utility class for grouping service instances

    Useful for deploying services in group whilst
    keeping a central view of all services in a workload
    """

    @property
    def name(self):
        return GroupNameUtility.resolve_group_name(self._name)

    def __init__(self, name: Union[str, EnvValue]):
        self._name = None

        if isinstance(name, str):
            self._name = name

        if isinstance(name, EnvValue):
            self._name = name

        if self._name is None:
            raise Exception(f"Expecting a valid name, got: {name}")

    def append(self, what: Union[GCPService, Callable]):
        assert isinstance(what, GCPService) or callable(what)
        return super().append(what)

    add = append
    __add__ = append


class ServiceGroups(list):
    """
    Container utility class for groups

    The use case is for a Deployer to retrieve
    a target group of services to deploy

    Since it's base class is a list, just
    'append' to it but the more typical use
    case would be to use the `create` method
    so that the groups are properly tracked.
    """

    def __init__(self):
        super().__init__()
        self._map = dict()

    def clear(self):
        super().clear()
        self._map.clear()

    @property
    def all(self):
        return self._map

    def __getitem__(self, what: Union[str, GroupName]):
        str_name = GroupNameUtility.resolve_group_name(what)
        return self._map[str_name]

    def get(self, what, default):
        str_name = GroupNameUtility.resolve_group_name(what)
        return self._map.get(str_name, default)

    def create(self, name: GroupName) -> ServiceGroup:
        """
        Create or retrieve a group by name
        """
        str_name = GroupNameUtility.resolve_group_name(name)

        if (group := self._map.get(str_name, None)) is not None:
            return group

        # create a new one and keep track of it
        group = ServiceGroup(name)

        self._map[str_name] = group
        self.append(group)

        return group


# We only really need one group of groups
service_groups = ServiceGroups()


class _PolicyMeta(type):
    """
    Collect derived classes
    """

    @classmethod
    @property
    def derived_classes(cls):
        return cls.__all_classes__

    @classmethod
    def only_add_real_service_class(cls, classe):
        new_class_name = classe.__name__.lower()

        if "mock" in new_class_name:
            return

        if new_class_name[0] == "_":
            return

        if not getattr(cls, "__all_classes__", False):
            setattr(cls, "__all_classes__", [])

        cls.__all_classes__.append(classe)

    def __new__(cls, name, bases, attrs):

        new_class = super().__new__(cls, name, bases, attrs)

        # Skip the base class
        if len(bases) > 0:
            cls.only_add_real_service_class(new_class)

        setattr(new_class, "_allowed", [])

        return new_class


class PolicyViolation(Exception):
    """Base class for all policy violations"""


class Policy(metaclass=_PolicyMeta):
    """
    The base class for all policies

    We are using class methods to simplify usage i.e.
    instead of having the user track policy instances
    in the build code
    """

    def __init__(self):
        raise Exception("Cannot be instantiated")

    @classmethod
    @property
    def name(cls):
        return cls.__name__

    @classmethod
    def allows(cls, service: GCPService):
        assert isinstance(service, GCPService)
        return service in cls._allowed

    @classmethod
    def allow(cls, service: GCPService, reason: str):
        assert isinstance(service, GCPService)
        assert isinstance(reason, str)

        logging.warning(f"The service '{service.name}' was "
                        f"allowed by default on policy '{cls.name}'")
        cls._allowed.append(service)
        return cls

    @classmethod
    def evaluate(cls, groups: List[ServiceGroup], service: GCPService):
        """
        NOTE must be implemented in derived classes

        NOTE Must raise an exception when policy is violated
        """
        raise NotImplementedError


@dataclass
class PolicingResult:
    """
    passed: True if the policy evaluation passed
    raised: when an exception was raised in DRY_RUN mode
    allowed: when skipped because policy allowed by default on service
    """

    service: GCPService
    policy: Policy
    violation: Union[PolicyViolation, None] = field(default=None)

    raised: bool = field(default=False)
    passed: bool = field(default=False)
    allowed: bool = field(default=False)


@dataclass
class PolicingResults:
    """
    outcome: the takeaway result - if passed => None
    results: the individual results
    """
    outcome: Union[PolicingResult, None]
    results: List[PolicingResult]

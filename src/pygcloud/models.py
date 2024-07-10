"""
@author: jldupont
"""
import os
from typing import List, Tuple, NewType, Union, Callable
from abc import ABC, abstractmethod
from dataclasses import dataclass
from .constants import ServiceCategory
from .helpers import validate_name


class EnvValue(str):
    """
    Retrieve a value from an environment variable
    """
    def __new__(cls, name):
        value = os.environ.get(name)
        instance = super().__new__(cls, value)
        return instance


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
    def __init__(self, key: str, env_var_name: str):
        """
        key: parameter name
        env_var_name: environment variable name
        """
        assert isinstance(key, str)
        assert isinstance(env_var_name, str)

        value = os.environ.get(env_var_name, None)
        if value is None:
            raise ValueError(f"Environment variable {env_var_name} not found")
        super().__init__(key, value)


Params = NewType("Param", Union[List[Tuple[str, str]], List[Param]])
Label = NewType("Label", Tuple[str, str])
GroupName = NewType("GroupName", Union[str, EnvValue])


class GroupNameUtility:

    @staticmethod
    def is_of_type(what: GroupName):
        return isinstance(what, str) or \
            isinstance(what, EnvValue)

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


class ServiceNode(ABC):
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
    """
    SERVICE_CATEGORY = ServiceCategory.INDETERMINATE
    REQUIRES_UPDATE_AFTER_CREATE = False
    REQUIRES_DESCRIBE_BEFORE_CREATE = False

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
        if name is not None:
            if not validate_name(name):
                raise Exception(f"Invalid name: {name}")

        self.already_exists = None  # indeterminated
        self.last_result = None
        self._name = name
        self._ns = ns
        self._uses: List[ServiceNode] = []

    def use(self, service: ServiceNode):
        self._uses.append(service)
        return self

    @property
    def uses(self) -> List[ServiceNode]:
        return self._uses

    def __repr__(self):
        return f"""
        {self.__class__.__name__}
        (already_exists={self.already_exists},
        last_result={self.last_result}
        )
        """.strip()

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
        if result.success:
            self.already_exists = True
        return result

    def after_create(self, result: Result) -> Result:
        self.last_result = result
        return result

    def after_update(self, result: Result) -> Result:
        self.last_result = result
        return result

    def after_delete(self, result: Result) -> Result:
        self.last_result = result
        return result


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
            self.already_exists = False
            return result

        # Case 2: Check if the service already exists
        if "already_exists" in result.message.lower():

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
        assert isinstance(what, GCPService) or \
            isinstance(what, Callable)
        return super().append(what)


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

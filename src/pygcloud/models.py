"""
@author: jldupont
"""
from typing import List, Tuple, NewType, Union
from dataclasses import dataclass
from .constants import ServiceCategory


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


Params = NewType("Param", Union[List[Tuple[str, str]], List[Param]])


@dataclass(frozen=True)
class Result:
    success: bool
    message: str
    code: int


class GCPService:

    SERVICE_CATEGORY = ServiceCategory.INDETERMINATE

    @property
    def category(self):
        return self.SERVICE_CATEGORY

    def __init__(self):
        self.already_exists = None  # indeterminated
        self.last_result = None

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
        if "ALREADY_EXISTS" in result.message:
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

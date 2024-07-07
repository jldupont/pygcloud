"""
@author: jldupont
"""
from typing import List, Tuple, TypeAlias
from dataclasses import dataclass


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


Params: TypeAlias = List[Tuple[str, str] | List[Param]]


@dataclass(frozen=True)
class Result:
    success: bool
    message: str
    code: int


class GCPService:

    def __init__(self):
        self.already_exists = None  # indeterminated
        self.last_result = None

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

    def after_describe(self, result: Result):
        self.last_result = result
        if result.success:
            self.already_exists = True
        return self

    def after_create(self, result: Result):
        self.last_result = result
        return self

    def after_update(self, result: Result):
        self.last_result = result
        return self

    def after_delete(self, result: Result):
        self.last_result = result
        return self

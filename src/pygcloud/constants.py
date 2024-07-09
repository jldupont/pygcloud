"""@author: jldupont"""
from enum import Enum

__all__ = ["ServiceCategory"]


class ServiceCategory(Enum):
    INDETERMINATE = "indeterminate"
    SINGLETON_IMMUTABLE = "singleton_immutable"
    REVISION_BASED = "revision_based"
    UPDATABLE = "updateable"

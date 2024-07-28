"""
@author: jldupont
"""

from typing import Set, TypeVar


T = TypeVar("T")


class BaseType(type):
    """
    Collect derived classes

    The derived classes with names containing
    the string "mock" or beginning with an underscore
    are ignored: this helps with unit-testing.

    The base class itself is also not collected.
    """

    __all_classes__: Set[T] = []

    @classmethod
    @property
    def derived_classes(cls) -> Set[T]:
        return cls.__all_classes__

    @classmethod
    def only_add_pertinent_class(cls, classe: T):
        new_class_name = classe.__name__.lower()

        if "mock" in new_class_name:
            return

        if new_class_name[0] == "_":
            return

        cls.__all_classes__.append(classe)

    def __new__(cls, name, bases, attrs):

        new_class = super().__new__(cls, name, bases, attrs)

        # Skip the base class
        if len(bases) > 0:
            cls.only_add_pertinent_class(new_class)

        return new_class

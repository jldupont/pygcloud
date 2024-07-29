"""
@author: jldupont
"""

from typing import Set, TypeVar, Type


T = TypeVar("T")


class BaseType(type):
    """
    Collect derived classes

    The derived classes with names containing
    the string "mock" or beginning with an underscore
    are ignored: this helps with unit-testing.

    The base class itself is also not collected.
    """

    __all_classes__: Set[Type[T]] = set()
    __all_instances__: Set[T] = set()
    __all_names__: Set[str] = set()

    @classmethod
    @property
    def derived_classes(cls) -> Set[Type[T]]:
        return cls.__all_classes__

    @classmethod
    def only_add_pertinent_class(cls, classe: Type[T]):
        new_class_name = classe.__name__.lower()

        if "mock" in new_class_name:
            return

        if new_class_name[0] == "_":
            return

        cls.__all_classes__.add(classe)

    def __new__(cls, name, bases, attrs):
        """
        This tracks the creation of new derived classes
        """
        new_class = super().__new__(cls, name, bases, attrs)

        # Skip the base class
        if len(bases) > 0:
            cls.only_add_pertinent_class(new_class)

        return new_class

    @classmethod
    def _process_instance(cls, instance):
        if not hasattr(instance, "name"):
            raise Exception(f"Instance '{instance}' has no 'name' attribute")

        if instance.name in cls.__all_names__:
            raise Exception(f"{cls.__name__} already has an instance of name: {instance.name}")

        cls.__all_instances__.add(instance)
        cls.__all_names__.add(instance.name)

    @classmethod
    def all(cls):
        return cls.__all_instances__

    def __iter__(self):
        """This allows iterating over the class"""
        return iter(self.__all_instances__)

    @classmethod
    def clear(cls):
        cls.__all_instances__.clear()
        cls.__all_names__.clear()

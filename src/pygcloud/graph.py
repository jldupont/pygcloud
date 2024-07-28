"""
# Graph module

@author: jldupont
"""

from typing import Union, Set, Type
from enum import Enum
from dataclasses import dataclass, field
from .models import ServiceNode
from .base_types import BaseType


Str = Union[str, None]


class Relation(Enum):
    """
    USES: when it is explicit that a node uses another node
    USED_BY: equivalent to "USES" but in reverse
    PARENT_IS: used with "organizations", "projects" and "folders"
    HAS_ACCESS: related to IAM bindings
    """

    USES = "uses"
    USED_BY = "used_by"
    PARENT_IS = "parent_is"
    HAS_ACCESS = "has_access"


@dataclass
class Node:
    """
    Node type

    Only the service type is exposed in order
    to maximize our chances of backward compatibility
    as the API evolves. If we expose too much information
    outright, it will be difficult to course correct without
    introducing breaking changes.
    """

    name: str
    kind: Type[ServiceNode]

    def __post_init__(self):
        assert issubclass(self.kind, ServiceNode)

    def __hash__(self):
        """This cannot be moved to base class"""
        return hash(self.name)


@dataclass
class Group(metaclass=BaseType):
    """
    A bare minimum definition of the group type

    Derived class declarations will be collected automatically
    and available using 'Group.derived_classes' attribute
    """

    name: Str
    members: Set[Node] = field(default_factory=set)

    def add(self, member: Node):
        assert isinstance(member, Node), print(f"Got: {member}")
        self.members.add(member)
        return self

    def __len__(self):
        return len(self.members)

    def __contains__(self, member: Node):
        """Supporting the 'in' operator"""
        assert isinstance(member, Node), print(f"Got: {member}")
        return member in self.members


@dataclass
class Edge:
    """
    An edge between two nodes
    """

    relation: Relation
    source: Union[Node, Group]
    target: Union[Node, Group]

    def __post_init__(self):
        assert isinstance(self.source, (Node, Group))
        assert isinstance(self.target, (Node, Group))
        assert isinstance(self.relation, Relation)

    def __hash__(self):
        vector = f"{self.source.name}-{self.relation.value}-{self.target.name}"
        return hash(vector)

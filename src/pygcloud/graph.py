"""
Graph module

The "group" construct can be represented through various means:

* Dedicated class containing a list of Nodes
* A virtual Node (derived from Node) with edges to it
* Node class with a list of group names

Since "group" amounts to being just an abstract construct, the option to use
a "virtual node" would change this nature. The same goes for the dedicated class IMO.

The last option to use a list of labels appears more aligned with the abstract nature of "group".

@author: jldupont
"""
from typing import Union, Set, Type
from enum import Enum
from dataclasses import dataclass, field
from pygcloud.models import ServiceNode


EdgeKind = Union[str, None]
Str = Union[str, None]


class Relation(Enum):
    USES = "uses"
    USED_BY = "used_by"
    PARENT_IS = "parent_is"


@dataclass
class Node:
    """
    kind: to further qualify the node type
    """
    name: str
    service_type: Type[ServiceNode]
    groups: Set[str] = field(default_factory=set)


@dataclass
class Edge:
    """
    An edge between two nodes

    kind: to further qualify the relation type
    """
    kind: EdgeKind
    relation: Relation
    source: Node
    dest: Node

"""
@author: jldupont
"""
import pytest  # NOQA
from pygcloud.graph import Group, Node, Edge, Relation
from pygcloud.models import ServiceNode
from pygcloud.base_types import BaseType


class MockGroup(Group):
    ...


class MockServiceNode(ServiceNode):
    ...


class MockNode(Node):
    ...


def test_group_base_type():

    assert isinstance(Group, type)
    assert not issubclass(Group, BaseType), print(Group.__class__)
    assert Group.__class__ == BaseType

    assert issubclass(MockGroup, Group)


def test_group_base_class_ignored():
    assert 'Group' not in Group.derived_classes


def test_group_mock_ignored():
    assert 'MockGroup' not in Group.derived_classes


def test_group_iterate_instances():

    Group.clear()

    g1 = MockGroup(name="g1")
    g2 = MockGroup(name="g2")

    s = set({g1, g2})

    assert Group.all() == s

    a = set(list(Group))

    assert a == s


def test_group_user_defined_group():

    Group.clear()

    # The name needs to be extracted from the ServiceNode
    # in scope: we do not want to surface the whole service node
    # for "Separation Of Concerns".
    mn = MockNode(name="mock_node", kind=MockServiceNode)

    g = MockGroup(name="user_group")
    g.add(mn)

    assert len(g) == 1
    assert g.name == "user_group"
    assert mn in g


def test_edge_basic():

    Edge.clear()

    assert len(Edge.all()) == 0

    n1 = MockNode(name="n1", kind=MockServiceNode)
    n2 = MockNode(name="n2", kind=MockServiceNode)

    e12 = Edge(relation=Relation.HAS_ACCESS, source=n1, target=n2)

    assert e12 in Edge.all()


def test_edge_idempotence():

    Edge.clear()

    n1 = MockNode(name="n1", kind=MockServiceNode)
    n2 = MockNode(name="n2", kind=MockServiceNode)

    e12 = Edge(relation=Relation.HAS_ACCESS, source=n1, target=n2)

    with pytest.raises(Exception):
        Edge(relation=Relation.HAS_ACCESS, source=n1, target=n2)

    # __repr__ test
    print(e12)


def test_edge_set_nodes():

    Edge.clear()
    Group.clear()

    n1 = MockNode(name="n1", kind=MockServiceNode)
    n2 = MockNode(name="n2", kind=MockServiceNode)
    n3 = MockNode(name="n3", kind=MockServiceNode)

    e12 = Edge(relation=Relation.HAS_ACCESS, source=n1, target=n2)
    e13 = Edge(relation=Relation.PARENT_IS, source=n1, target=n3)

    edges = set()

    edges.add(e12)
    edges.add(e13)

    assert len(edges) == 2


def test_edge_set_groups():
    """Edges between Groups"""

    Edge.clear()
    Group.clear()

    g1 = MockGroup(name="g1")
    g2 = MockGroup(name="g2")

    Edge(relation=Relation.HAS_ACCESS, source=g1, target=g2)
    Edge(relation=Relation.HAS_ACCESS, source=g2, target=g1)

    edges = set()
    for edge in Edge:
        edges.add(edge)

    assert Edge.all() == edges


def test_group_idempotence():

    Group.clear()
    MockGroup(name="mock_group")

    with pytest.raises(Exception):
        # Attempt to reuse name already taken
        MockGroup(name="mock_group")

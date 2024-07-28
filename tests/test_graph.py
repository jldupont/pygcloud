"""
@author: jldupont
"""
import pytest  # NOQA
from pygcloud.graph import Group, Node, Edge, Relation
from pygcloud.models import ServiceNode


class MockGroup(Group):
    ...


class MockServiceNode(ServiceNode):
    ...


class MockNode(Node):
    ...


def test_group_base_class_ignored():
    assert 'Group' not in Group.derived_classes


def test_group_mock_ignored():
    assert 'MockGroup' not in Group.derived_classes


def test_group_user_defined_group():

    # The name needs to be extracted from the ServiceNode
    # in scope: we do not want to surface the whole service node
    # for "Separation Of Concerns".
    mn = MockNode(name="mock_node", kind=MockServiceNode)

    g = MockGroup(name="user_group")
    g.add(mn)

    assert len(g) == 1
    assert g.name == "user_group"
    assert mn in g


def test_edge_set_nodes():

    n1 = MockNode(name="n1", kind=MockServiceNode)
    n2 = MockNode(name="n2", kind=MockServiceNode)
    n3 = MockNode(name="n3", kind=MockServiceNode)

    e12 = Edge(relation=Relation.HAS_ACCESS, source=n1, target=n2)
    e13 = Edge(relation=Relation.HAS_ACCESS, source=n1, target=n3)

    edges = set()

    edges.add(e12)
    edges.add(e13)

    assert len(edges) == 2


def test_edge_set_groups():

    g1 = MockGroup(name="g1")
    g2 = MockGroup(name="g2")

    e12 = Edge(relation=Relation.HAS_ACCESS, source=g1, target=g2)
    edges = set()

    edges.add(e12)
    assert len(edges) == 1

    # Idempotency check (very much native to set() but
    # my defensive coding reflexes are kicking-in)
    edges.add(e12)
    assert len(edges) == 1

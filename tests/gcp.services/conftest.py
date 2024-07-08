"""
@author: jldupont
"""
import pytest
from pygcloud.models import ServiceNode
from pygcloud.gcp.labels import LabelGenerator
from pygcloud.models import GCPService


class MockServiceNode(GCPService, LabelGenerator):
    ...


@pytest.fixture
def mock_sn():
    return MockServiceNode("name", "ns")


class MockSn(ServiceNode):
    def __init__(self, name, ns):
        self._name = name
        self._ns = ns

    @property
    def name(self):
        return self._name

    @property
    def ns(self):
        return self._ns


@pytest.fixture
def sn1():
    return MockSn("name1", "ns1")


@pytest.fixture
def sn2():
    return MockSn("name2", "ns2")


@pytest.fixture
def sn3():
    return MockSn("name3", "ns3")

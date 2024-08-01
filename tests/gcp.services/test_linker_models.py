"""
@author: jldupont
"""
import pytest  # NOQA
from pygcloud.graph_models import Node, Edge
from pygcloud.gcp.linker_models import process_refs


def test_users(mock_services_address, mock_ip_address):
    Node.clear()
    result = process_refs(mock_services_address)
    node: Node = result[0]
    assert node.name in mock_ip_address.selfLink, print(result)

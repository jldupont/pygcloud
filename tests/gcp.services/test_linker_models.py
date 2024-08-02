"""
@author: jldupont
"""
import pytest  # NOQA
from pygcloud.graph_models import Node  # , Edge
from pygcloud.gcp.services.fwd_rules import FwdRuleHTTPSProxyService
from pygcloud.gcp.linker_models import process_refs


@pytest.mark.skip
def test_users(mock_services_address, mock_ip_address):
    Node.clear()
    result = process_refs(mock_services_address)

    #
    # The IPaddress first
    #
    node1: Node = result[0]
    assert node1.name in mock_ip_address.selfLink, print(result)

    #
    # Followed by the ref to the FwdRule
    #
    node2 = result[1]
    assert node2.kind == FwdRuleHTTPSProxyService, print(node2)

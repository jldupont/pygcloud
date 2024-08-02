"""
@author: jldupont
"""
import pytest
from pygcloud import events
from pygcloud.models import Result
from pygcloud.deployer import Deployer
from pygcloud.gcp.linker import Linker
from pygcloud.gcp.models import Ref, RefSelfLink, RefUses, RefUsedBy
from pygcloud.graph_models import Node, Edge, Relation
from pygcloud.gcp.services.fwd_rules import FwdRuleHTTPSProxyService
from pygcloud.gcp.services.addresses import ServicesAddress


@pytest.fixture
def result_success():
    return Result(
        success=True,
        message="",
        code=0
    )


@pytest.fixture
def mock_deployer():
    return Deployer()


def test_linker_simple(mock_deployer, result_success, mock_services_address_gen):
    Linker.clear()

    # We need to do a proper reset before creating stuff
    srv = mock_services_address_gen()  # NOQA

    # pretend it was deployed
    Linker.add(srv)

    refs = Ref.all

    # We should have 1 SelfLink and 1 RefUses
    assert len(refs) == 2, print(refs)

    selfLink = refs[0]
    assert isinstance(selfLink, RefSelfLink), print(selfLink)

    user = refs[1]
    assert isinstance(user, RefUsedBy), print(user)

    events.end_deploy(mock_deployer, "mock_sg", result_success)

    #
    # We should have 2 Nodes: ServicesAddress and "user" ForwardingRule
    #
    nodes = Node.all
    assert len(nodes) == 2, print(nodes)

    # We should have 1 Edge
    assert len(Edge.all) == 1, print(Edge.all)

    edge = Edge.all[0]
    assert isinstance(edge, Edge), print(edge)

    #
    # The IP Addess is "used by" the FwdRuleHTTPSProxyService
    #
    assert edge.relation == Relation.USED_BY
    assert edge.source.kind == ServicesAddress, print(edge.source)
    assert edge.target.kind == FwdRuleHTTPSProxyService, print(edge.target)

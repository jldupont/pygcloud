"""
@author: jldupont
"""
import pytest
from pygcloud import events
from pygcloud.models import Result, GCPServiceInstanceNotAvailable, \
    GCPService, GCPServiceUnknown
from pygcloud.deployer import Deployer
from pygcloud.gcp.linker import Linker
from pygcloud.gcp.models import Ref, RefSelfLink, RefUsedBy, UnknownRef
from pygcloud.graph_models import Node, Edge, Relation
from pygcloud.gcp.services.fwd_rules import FwdRuleHTTPSProxyService
from pygcloud.gcp.services.addresses import ServicesAddress
from pygcloud.gcp.services.proxies import HTTPSProxyService
from pygcloud.gcp.catalog import lookup_service_class_from_ref


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


class MockEdge(Edge):
    def __eq__(self, other):
        return self.relation == other.relation and \
            self.source == other.source and \
            self.target == other.target


class MockService(GCPService):
    ...


@pytest.fixture
def mock_service():
    return MockService("mock_service")


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
    # The IP Addess is "used by" the FwdRuleHTTPSProxyService but
    #  the latter is not deployed
    #
    assert edge.relation == Relation.USED_BY
    assert edge.source.kind == ServicesAddress, print(edge.source)
    assert edge.target.kind == FwdRuleHTTPSProxyService, print(edge.target)
    assert isinstance(edge.target.obj, GCPServiceInstanceNotAvailable), \
        print(edge.target.obj)


def test_linker_full_edge(mock_services_address_gen,
                          mock_https_proxy_gen,
                          mock_deployer,
                          result_success):
    Linker.clear()

    proxy_srv = mock_https_proxy_gen()
    ip_srv = mock_services_address_gen()

    Linker.add(proxy_srv)
    Linker.add(ip_srv)

    events.end_deploy(mock_deployer, "mock_sg", result_success)

    # ServicesAddress, FwdRule, HTTPSProxy, UrlMap, SSLCertificate
    assert len(Node.all) == 5, print(Node.all)

    # IP    --UsedBy--> FwdRule
    # Proxy --uses-->   Certificate
    # Proxy --uses-->   UrlMap
    assert len(Edge.all) == 3, print(Edge.all)

    e0 = Edge.all[0]
    e1 = Edge.all[1]
    e2 = Edge.all[2]

    assert repr(e0) == \
        "Edge(ingress-proxy-ip, used_by, fwd-proxy-service)"
    assert isinstance(e0.source.obj, ServicesAddress), print(e0.source)
    assert isinstance(e0.target.obj, GCPServiceInstanceNotAvailable), print(e0.target)

    assert repr(e1) == \
        "Edge(proxy-service, uses, proxy-certificate)"
    assert isinstance(e1.source.obj, HTTPSProxyService), print(e1.source)
    assert isinstance(e1.target.obj, GCPServiceInstanceNotAvailable), print(e1.target)

    assert repr(e2) == \
        "Edge(proxy-service, uses, urlmap-backend-service)"
    assert isinstance(e2.source.obj, HTTPSProxyService), print(e2.source)
    assert isinstance(e2.target.obj, GCPServiceInstanceNotAvailable), print(e2.target)


def test_linker_unknown_service(mock_service, mock_deployer, result_success):
    """A ref to an unknown service type"""

    Linker.clear()
    Node.clear()
    Edge.clear()
    Ref.clear()

    RefSelfLink(
        project="project",
        region="region",
        name=mock_service.name,
        service_type="service_type_whatever",
        origin_service=mock_service
    )

    events.end_deploy(mock_deployer, "mock", result_success)

    print(Ref.all)
    assert len(Node.all) == 1, print(Node.all)
    assert len(Ref.all) == 1, print(Ref.all)

    ref0 = Ref.all[0]

    srv_class = lookup_service_class_from_ref(ref0)
    assert srv_class == GCPServiceUnknown


def test_linker_unknown_ref():
    invalid_link = "/whatever/something"

    with pytest.raises(UnknownRef):
        Ref.from_link(invalid_link)

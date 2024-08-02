"""
@author: jldupont
"""
from pygcloud.models import Result
from pygcloud.gcp.services.addresses import ServicesAddress
from pygcloud.gcp.models import IPAddress, Ref
from samples import IP_ADDRESS


class MockServicesAddress(ServicesAddress):

    def after_describe(self, result):
        result = Result(success=False, message="failure", code=1)
        self.last_result = result
        return result

    def after_create(self, result):
        result = Result(success=True, message=IP_ADDRESS, code=0)
        return super().after_create(result)


def test_services_address_create(deployer, mock_sg):
    """
    Also does Ref level testing
    """
    Ref.clear()

    srv = MockServicesAddress("ip_address")
    mock_sg.append(srv)

    deployer.deploy(mock_sg)

    assert isinstance(srv.spec, IPAddress), print(srv.spec)

    ip: IPAddress = srv.spec

    assert isinstance(ip.users, list), print(ip)

    ip0 = ip.users[0]
    assert isinstance(ip0, Ref), print(ip0)
    assert ip0.origin_service == srv

"""
@author: jldupont
"""
from pygcloud.models import Result
from pygcloud.gcp.services.addresses import ServicesAddress
from pygcloud.gcp.models import IPAddress
from samples import IP_ADDRESS


class MockServicesAddress(ServicesAddress):

    def after_describe(self, result):
        result = Result(success=False, message="failure", code=1)
        self.last_result = result
        return result

    def after_create(self, result):
        result = Result(success=True, message=IP_ADDRESS, code=0)
        return super().after_create(result)


def test_services_address_create(deployer):

    srv = MockServicesAddress("ip_address")

    deployer.deploy(srv)

    assert isinstance(srv.spec, IPAddress), print(srv.spec)

"""
@author: jldupont
"""
from pygcloud.gcp.models import IPAddress


def test_service_address(sample_ip_json):

    ip = IPAddress.from_json_string(sample_ip_json)
    assert ip.name == "ingress-proxy-ip"
    assert ip.address == "34.144.203.24"

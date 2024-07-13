"""
@author: jldupont
"""
from pygcloud.gcp.models import IPAddress, CloudRunRevisionSpec


def test_service_address(sample_ip_json):

    ip = IPAddress.from_json_string(sample_ip_json)
    assert ip.name == "ingress-proxy-ip"
    assert ip.address == "34.144.203.24"


def test_cloud_run_revision_spec(sample_cloud_run_revision_spec):

    crr = \
        CloudRunRevisionSpec.from_string(sample_cloud_run_revision_spec)

    assert crr.name == "SERVICE"
    assert crr.url == "https://SERVICE-4ro7a33l3a-nn.a.run.app"

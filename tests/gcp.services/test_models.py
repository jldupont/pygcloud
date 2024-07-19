"""
@author: jldupont
"""
import pytest
from pygcloud.gcp.models import IPAddress, CloudRunRevisionSpec, \
    BackendServiceSpec, BackendGroup, FwdRule, SSLCertificate, \
    HTTPSProxy, SchedulerJob, PubsubTopic, ServiceDescription, \
    FirestoreDb, ProjectDescription


def test_project_desc(sample_project_desc):
    p = ProjectDescription.from_string(sample_project_desc)
    assert p.projectNumber == "215695389495"
    assert p.parent["id"] == "116975272573"


def test_service_address(sample_ip_json):

    ip = IPAddress.from_string(sample_ip_json)
    assert ip.name == "ingress-proxy-ip"
    assert ip.address == "34.144.203.24"


def test_cloud_run_revision_spec(sample_cloud_run_revision_spec):

    crr = \
        CloudRunRevisionSpec.from_string(sample_cloud_run_revision_spec)

    assert crr.name == "SERVICE"
    assert crr.url == "https://SERVICE-4ro7a33l3a-nn.a.run.app"


def test_backend_service(sample_backend_service):

    bes = BackendServiceSpec.from_string(sample_backend_service)

    assert bes.name == "backend-service"
    assert bes.protocol == "HTTPS"

    groups = bes.backend_groups

    assert len(groups) == 1

    group = groups[0]
    assert isinstance(group, BackendGroup)

    assert group.capacityScaler == 1.0


@pytest.fixture
def fwd_rule(sample_fwd_rule):
    return FwdRule.from_string(sample_fwd_rule)


def test_fwd_rule(fwd_rule):
    assert fwd_rule.portRange == "443-443"


def test_fwd_rule_compare(sample_fwd_rule, fwd_rule):
    f2 = FwdRule.from_string(sample_fwd_rule)

    assert f2 == fwd_rule

    # We will want to compare, sometimes, fwd rules
    # without incurring the complexity of computing
    # the target
    f2.target = None
    fwd_rule.target = None

    assert f2 == fwd_rule

    # A little bit of paranoia...
    assert f2.target is None
    assert fwd_rule.target is None


def test_ssl_certificate(sample_ssl_certificate):

    c = SSLCertificate.from_string(sample_ssl_certificate)
    assert c.type == "MANAGED"
    assert c.managed["domains"] == ["DOMAIN"], print(c.managed)


def test_https_proxy(sample_https_proxy):

    p = HTTPSProxy.from_string(sample_https_proxy)
    assert len(p.sslCertificates) == 1
    assert p.name == "proxy-service"


def test_scheduler_job(sample_scheduler_job):

    j = SchedulerJob.from_string(sample_scheduler_job)
    assert 'topics/test' in j.pubsubTarget["topicName"]
    assert j.name == "test-job"
    assert j.location == "northamerica-northeast1"


def test_pubsub_topic(sample_pubsub_topic):

    t = PubsubTopic.from_string(sample_pubsub_topic)
    assert t.name == "test"


def test_services_list(sample_services_list):

    liste = ServiceDescription.from_json_list(sample_services_list)

    first = liste[0]

    assert first.api == "aiplatform.googleapis.com"
    assert first.project_number == "215695389495"


def test_firestore_db(sample_firestore_db):

    d = FirestoreDb.from_string(sample_firestore_db)
    assert d.name == "(default)"

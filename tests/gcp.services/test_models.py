"""
@author: jldupont
"""
import pytest
from pygcloud.models import Spec
from pygcloud.gcp.models import Ref, LinksMap, IPAddress, CloudRunRevisionSpec, \
    BackendServiceSpec, BackendGroup, FwdRule, SSLCertificate, \
    HTTPSProxy, SchedulerJob, PubsubTopic, ServiceDescription, \
    FirestoreDb, ProjectDescription, TaskQueue, UrlMap, \
    ServiceAccountSpec, IAMPolicy, IAMBinding, GCSBucket, ACL


def test_spec_contains_derived_class_types():
    assert len(Spec.derived_class_types) >= 21, print(Spec.derived_class_types)


@pytest.mark.parametrize("input,expected", [
    ("https://www.googleapis.com/compute/beta/projects/PROJECT/regions/northamerica-northeast1",
        Ref(region="northamerica-northeast1", project="PROJECT")),
    ("https://www.googleapis.com/compute/v1/projects/PROJECT/global/addresses/ingress-proxy-ip",
        Ref(region="global", project="PROJECT", service_type="addresses", name="ingress-proxy-ip")),
    ("https://www.googleapis.com/compute/v1/projects/PROJECT/regions/na1/networkEndpointGroups/backend-neg",
        Ref(region="na1", project="PROJECT", service_type="networkEndpointGroups", name="backend-neg"))
])
def test_ref(input, expected):
    result = Ref.from_link(input)
    assert result == expected, print(result)


def test_links_single_set():

    links = LinksMap()
    links["key"] = "value"

    with pytest.raises(ValueError):
        links["key"] = 666

    assert "key" in links

    with pytest.raises(ValueError):
        del links['key']


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
    assert crr.service_account == "215695389495-compute@developer.gserviceaccount.com"


def test_cloud_run_revision_spec_list(sample_cloud_run_revision_spec):

    liste = f"[{sample_cloud_run_revision_spec}]"

    liste = \
        CloudRunRevisionSpec.from_json_list(liste)

    assert len(liste) == 1

    crr = liste[0]

    assert crr.name == "SERVICE"
    assert crr.url == "https://SERVICE-4ro7a33l3a-nn.a.run.app"


def test_backend_service(sample_backend_service):

    bes = BackendServiceSpec.from_string(sample_backend_service)

    assert bes.name == "backend-service"
    assert bes.protocol == "HTTPS"

    groups = bes.backends

    """
    import typing

    t = bes.__annotations__["backends"]

    origin = typing.get_origin(t)
    assert origin == list

    args = typing.get_args(t)
    arg0 = args[0]
    print(args)
    assert arg0 == BackendGroup
    """

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
    assert j.topicName == "projects/PROJECT/topics/test"


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


def test_task_queue(sample_task_queue):

    q = TaskQueue.from_string(sample_task_queue)
    assert q.name == "test"
    assert q.location == "northamerica-northeast1"


def test_to_dict(sample_task_queue):

    q = TaskQueue.from_string(sample_task_queue)
    d = q.to_dict()

    assert d['retryConfig']['maxAttempts'] == 1

    import json

    j = json.dumps(d)

    assert 'RUNNING' in j


def test_backend_service_to_json(sample_backend_service):
    """
    This checks that the `to_json` method works recursively
    using the FlexJSONEncoder
    """
    bes = BackendServiceSpec.from_string(sample_backend_service)

    js = bes.to_json_string()
    assert isinstance(js, str), print(js)

    import json
    jso = json.loads(js)
    assert isinstance(jso, dict)


def test_url_map(sample_url_map):

    um = UrlMap.from_string(sample_url_map)
    assert um.name == "urlmap-backend-service"


def test_service_account_spec(sample_service_account_spec):

    sa = ServiceAccountSpec.from_string(sample_service_account_spec)
    assert sa.name == "215695389495-compute@developer.gserviceaccount.com"
    assert sa.is_default()


def test_iam_policy(sample_bucket_iam_policy):

    p = IAMPolicy.from_json_list(sample_bucket_iam_policy)
    assert isinstance(p, IAMPolicy)

    first = p.bindings[0]

    assert first.role == "roles/storage.legacyBucketOwner"
    assert len(first.members) == 2, print(first)

    m0 = first.members[0]
    assert m0.email == "PROJECT", print(m0)

    tb = IAMBinding(
        ns="projectViewer",
        email="PROJECT",
        role="roles/storage.legacyObjectReader"
        )

    assert p.contains(tb)


def test_iam_policy_empty_bindings(sample_empty_bindings):

    p = IAMPolicy.from_json_list(sample_empty_bindings)

    assert len(p.bindings) == 0


def test_iam_policy_empty_bindings2(sample_empty_bindings):

    p = IAMPolicy.from_string(sample_empty_bindings)

    assert len(p.bindings) == 0


def test_gcs_bucket(sample_gcs_bucket):
    b = GCSBucket.from_string(sample_gcs_bucket)

    assert b.acl is not None
    assert isinstance(b.acl[0], ACL), print(b.acl)

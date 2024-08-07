"""
@author: jldupont
"""

import pytest
from pygcloud.gcp.labels import LabelGenerator
from pygcloud.models import GCPService, Result
from pygcloud.gcp.models import IAMBinding, IPAddress, HTTPSProxy
from samples import (
    PROJECT_BINDINGS,
    IP_ADDRESS,
    CLOUD_RUN_REVISION_SPEC,
    BACKEND_SERVICE,
    FWD_RULE,
    STORAGE_BUCKET,
    SSL_CERTIFICATE,
    HTTPS_PROXY,
    SCHEDULER_JOB,
    PUBSUB_TOPIC,
    SERVICES_LIST,
    FIRESTORE_DB,
    CLOUDRUN_NEG_SPEC,
    PROJECT_DESC,
    TASK_QUEUE_SPEC,
    URL_MAP_SPEC,
    SERVICE_ACCOUNT_SPEC,
    BUCKET_IAM_BINDINGS_SPEC,
    SAMPLE_EMPTY_BINDINGS,
)

# from pygcloud.gcp.services.iam import ServiceAccountIAM
from pygcloud.gcp.services.addresses import ServicesAddress
from pygcloud.gcp.services.proxies import HTTPSProxyService


@pytest.fixture
def sample_project_bindings():
    return PROJECT_BINDINGS


@pytest.fixture
def sample_project_desc():
    return PROJECT_DESC


"""
@pytest.fixture
def project_bindings():
    return ProjectIAMBindings(PROJECT_BINDINGS)
"""


@pytest.fixture
def sample_binding():
    """Exists in the samples"""
    return IAMBinding(
        email="280761648870@cloudbuild.gserviceaccount.com",
        role="roles/editor",
        ns="serviceAccount",
    )


@pytest.fixture
def sample_fake_binding():
    """Does not exist in the samples"""
    return IAMBinding(email="some_email", role="roles/editor", ns="user")


class MockServiceNode(GCPService, LabelGenerator): ...  # NOQA


@pytest.fixture
def mock_sn():
    return MockServiceNode("name", "ns")


class MockSn(MockServiceNode):
    def __init__(self, name, ns):
        self._name = name
        self._ns = ns

    @property
    def name(self):
        return self._name

    @property
    def ns(self):
        return self._ns


@pytest.fixture
def mock_sn_class():
    return MockSn


@pytest.fixture
def sn1():
    return MockSn("name1", "ns1")


@pytest.fixture
def sn2():
    return MockSn("name2", "ns2")


@pytest.fixture
def sn3():
    return MockSn("name3", "ns3")


"""
@pytest.fixture
def mock_service_account_iam_class():
    class MockServiceAccountIAM(ServiceAccountIAM):

        def before_describe(self):
            self.before_describe_called = True
            self.after_created_called = False

        def after_describe(self, result: Result) -> Result:
            result = Result(success=True, message=PROJECT_BINDINGS, code=0)
            super().after_describe(result)
            return result

        def before_create(self):
            super().before_create()
            print(self.already_exists)

        def after_create(self, result: Result) -> Result:
            self.after_created_called = True
            return result

    return MockServiceAccountIAM
"""


@pytest.fixture
def sample_ip_json():
    return IP_ADDRESS


@pytest.fixture
def result_success():
    return Result(success=True, message="success", code=0)


@pytest.fixture
def sample_cloud_run_revision_spec():
    return CLOUD_RUN_REVISION_SPEC


@pytest.fixture
def sample_backend_service():
    return BACKEND_SERVICE


@pytest.fixture
def sample_fwd_rule():
    return FWD_RULE


@pytest.fixture
def sample_gcs_bucket():
    return STORAGE_BUCKET


@pytest.fixture
def sample_ssl_certificate():
    return SSL_CERTIFICATE


@pytest.fixture
def sample_https_proxy():
    return HTTPS_PROXY


@pytest.fixture
def sample_scheduler_job():
    return SCHEDULER_JOB


@pytest.fixture
def sample_pubsub_topic():
    return PUBSUB_TOPIC


@pytest.fixture
def sample_services_list():
    return SERVICES_LIST


@pytest.fixture
def sample_firestore_db():
    return FIRESTORE_DB


@pytest.fixture
def sample_cloudrun_neg():
    return CLOUDRUN_NEG_SPEC


@pytest.fixture
def sample_task_queue():
    return TASK_QUEUE_SPEC


@pytest.fixture
def sample_url_map():
    return URL_MAP_SPEC


@pytest.fixture
def sample_service_account_spec():
    return SERVICE_ACCOUNT_SPEC


@pytest.fixture
def sample_bucket_iam_policy():
    return BUCKET_IAM_BINDINGS_SPEC


@pytest.fixture
def sample_empty_bindings():
    return SAMPLE_EMPTY_BINDINGS


@pytest.fixture
def mock_ip_address(sample_ip_json):
    return IPAddress.from_string(sample_ip_json)


@pytest.fixture
def mock_ip_address_gen(sample_ip_json):
    def gen():
        return IPAddress.from_string(sample_ip_json)

    return gen


@pytest.fixture
def mock_services_address_gen(sample_ip_json):
    """Affords us some time to perform resets"""

    def gen():
        # NOTE important ! MUST USE THE SAME NAME AS IN THE SAMPLE!
        mock = ServicesAddress(name="ingress-proxy-ip")
        ip = IPAddress.from_string(sample_ip_json, mock)
        mock.spec = ip
        return mock

    return gen


@pytest.fixture
def mock_services_address(mock_services_address_gen):
    return mock_services_address_gen()


@pytest.fixture
def mock_https_proxy_gen(sample_https_proxy):
    def gen():
        # name must be synchronized with the ServicesAddress above
        # and the sample
        mock = HTTPSProxyService(
            "proxy-service", "proxy-certificate", "urlmap-backend-service"
        )
        spec = HTTPSProxy.from_string(sample_https_proxy, mock)
        mock.spec = spec
        return mock

    return gen


@pytest.fixture
def sample_url_map_spec():
    return URL_MAP_SPEC

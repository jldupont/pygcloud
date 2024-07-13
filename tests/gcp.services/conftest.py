"""
@author: jldupont
"""
import pytest
from pygcloud.gcp.labels import LabelGenerator
from pygcloud.models import GCPService, Result
from pygcloud.gcp.parsers import ProjectIAMBindings, IAMBinding
from samples import PROJECT_BINDINGS, IP_ADDRESS, CLOUD_RUN_REVISION_SPEC
from pygcloud.gcp.services.iam import ServiceAccountIAM


@pytest.fixture
def project_bindings():
    return ProjectIAMBindings(PROJECT_BINDINGS)


@pytest.fixture
def sample_binding():
    """Exists in the samples"""
    return IAMBinding(
        email="280761648870@cloudbuild.gserviceaccount.com",
        role="roles/editor",
        ns="serviceAccount"
    )


@pytest.fixture
def sample_fake_binding():
    """Does not exist in the samples"""
    return IAMBinding(
        email="some_email",
        role="roles/editor",
        ns="user"
    )


class MockServiceNode(GCPService, LabelGenerator):
    ...


@pytest.fixture
def mock_sn():
    return MockServiceNode("name", "ns")


class MockSn(MockServiceNode):
    def __init__(self, name, ns):
        print(f"MockSn({ns}, {name})")
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


@pytest.fixture
def sample_ip_json():
    return IP_ADDRESS


@pytest.fixture
def result_success():
    return Result(success=True, message="success", code=0)


@pytest.fixture
def sample_cloud_run_revision_spec():
    return CLOUD_RUN_REVISION_SPEC

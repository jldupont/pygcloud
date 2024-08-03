import pytest
import os
from dataclasses import dataclass
from pygcloud.deployer import Deployer
from pygcloud.core import CommandLine
from pygcloud.models import GCPService, LazyEnvValue, service_groups, Spec, Result
from pygcloud.constants import ServiceCategory
from pygcloud.gcp.models import RefSelfLink


@pytest.fixture
def mock_sg():
    return service_groups.create("mock_sg")


@pytest.fixture
def env_first_key():
    return list(os.environ.keys())[0]


@pytest.fixture
def env_first_value(env_first_key):
    return os.environ[env_first_key]


@pytest.fixture
def lazy_env_value(env_first_key):
    return LazyEnvValue(env_first_key)


@dataclass
class MockSpec(Spec):
    selfLink: RefSelfLink


class MockGCPService(GCPService):
    SERVICE_CATEGORY = ServiceCategory.UPDATABLE
    SPEC_CLASS = MockSpec

    _COUNTER = 0

    def __init__(self, *p, **k):
        """
        Need a unique name or else
        we are getting in the way of the Linker
        """
        import uuid

        uid = str(uuid.uuid4())

        name = f"mock_name_{uid}"
        ns = "mock"

        super().__init__(name, ns=ns)

    def params_describe(self):
        return ["describe"]

    def after_describe(self, result: Result):

        count = self._COUNTER
        self._COUNTER += 1

        import json

        spec = {
            "selfLink": "/projects/mock_project"
            "/regions/mock_region"
            f"/mock_service_type/mock_{self.name}_{count}"
        }

        result = Result(success=True, message=json.dumps(spec), code=0)
        return super().after_describe(result)

    def params_create(self):
        return ["create"]

    def params_update(self):
        return ["update"]

    def after_create(self, result):
        super().after_create(result)
        self.create_result = result
        return result

    def after_update(self, result):
        super().after_update(result)
        self.update_result = result
        return result


@pytest.fixture
def mock_service_class():
    return MockGCPService


@pytest.fixture
def mock_service():
    return MockGCPService()


@pytest.fixture
def cmd_echo():
    return CommandLine("echo")


@pytest.fixture
def deployer(cmd_echo):
    return Deployer(cmd_echo)

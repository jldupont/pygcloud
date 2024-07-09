import pytest
import os
from pygcloud.deployer import Deployer
from pygcloud.core import CommandLine
from pygcloud.models import GCPService
from pygcloud.constants import ServiceCategory


@pytest.fixture
def env_first_key():
    return list(os.environ.keys())[0]


@pytest.fixture
def env_first_value(env_first_key):
    return os.environ[env_first_key]


class MockGCPService(GCPService):
    SERVICE_CATEGORY = ServiceCategory.UPDATABLE

    def params_describe(self):
        return [
            "describe"
        ]

    def params_create(self):
        return [
            "create"
        ]

    def params_update(self):
        return [
            "update"
        ]

    def after_describe(self, result):
        super().after_describe(result)
        self.describe_result = result
        return result

    def after_create(self, result):
        super().after_create(result)
        self.create_result = result
        return result

    def after_update(self, result):
        super().after_update(result)
        self.update_result = result
        return result


@pytest.fixture
def mock_service():
    return MockGCPService()


@pytest.fixture
def cmd_echo():
    return CommandLine("echo")


@pytest.fixture
def deployer(cmd_echo):
    return Deployer(cmd_echo)

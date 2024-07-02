"""@author: jldupont"""
import pytest
from pygcloud.models import GCPService, Result
from pygcloud.deployer import Deployer
from pygcloud.core import CommandLine

cmd_echo = CommandLine("echo")


class ServiceBase(GCPService):

    COMMON = [
        ("--param", "value"),
    ]

    def params_describe(self):
        return ["describe", "param_describe", self.COMMON]

    def params_create(self):
        return ["create", "param_create", self.COMMON]

    def params_update(self):
        return ["update", "param_update", self.COMMON]

    def after_create(self, result: Result):
        super().after_create(result)
        self.created = True

    def after_update(self, result: Result):
        super().after_update(result)
        self.updated = True


class ServiceAlreadyExists(ServiceBase):

    def before_describe(self):
        self.already_exists = True
        return self


class ServiceDoesNotExists(ServiceBase):

    def after_describe(self, _result: Result):
        self.already_exists = False
        return self


def test_deployer_already_exists():

    deployer = Deployer(cmd_echo)

    s = ServiceAlreadyExists()
    deployer.deploy(s)

    assert s.last_result.success
    assert s.updated

    with pytest.raises(AttributeError):
        assert s.created is None

    assert cmd_echo.last_command_args == \
        ["echo", "update", "param_update", "--param=value"]


def test_deployer_needs_creation():

    deployer = Deployer(cmd_echo)

    s = ServiceDoesNotExists()
    deployer.deploy(s)

    assert s.last_result.success
    assert s.created

    with pytest.raises(AttributeError):
        assert s.updated is not None

    assert cmd_echo.last_command_args == \
        ["echo", "create", "param_create", "--param=value"]

"""@author: jldupont"""
import pytest
from pygcloud.models import Result, Param, \
    GCPServiceSingletonImmutable, GCPServiceRevisionBased, GCPServiceUpdatable


@pytest.fixture
def common_params():
    return [Param("--common", "value")]


class ServiceUpdatable(GCPServiceUpdatable):

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
        result = super().after_create(result)
        self.created = True
        return result

    def after_update(self, result: Result):
        result = super().after_update(result)
        self.updated = True
        return result


class ServiceAlreadyExists(ServiceUpdatable):

    def before_describe(self):
        self.already_exists = True


class ServiceDoesNotExists(ServiceUpdatable):

    def after_describe(self, result: Result):
        self.already_exists = False
        return result


def test_deployer_already_exists(deployer):

    s = ServiceAlreadyExists("already_exists", "service")
    deployer.deploy(s)

    assert s.last_result.success
    assert s.updated

    with pytest.raises(AttributeError):
        assert s.created is None

    assert deployer.cmd.last_command_args == \
        ["echo", "update", "param_update", "--param", "value"]


def test_deployer_needs_creation(deployer):

    s = ServiceDoesNotExists()
    deployer.deploy(s)

    assert s.last_result.success
    assert s.created

    with pytest.raises(AttributeError):
        assert s.updated is not None

    assert deployer.cmd.last_command_args == \
        ["echo", "create", "param_create", "--param", "value"]


def test_deployer_with_common_params(deployer, common_params):

    deployer.set_common_params(common_params)

    s = ServiceAlreadyExists()
    deployer.deploy(s)

    assert deployer.cmd.last_command_args == \
        [
            "echo", "update", "param_update", "--param", "value",
            "--common", "value"]

# ==============================================================


class ServiceSingletonImmutable(GCPServiceSingletonImmutable):

    def __init__(self, state_exists: bool = False):
        super().__init__(name="Singleton", ns="service")
        self.state_exists = state_exists

    def params_describe(self):
        return ["describe", "param_describe"]

    def params_create(self):
        return ["create", "param_create"]

    def params_update(self):
        raise Exception("should not be called")

    def after_create(self, result: Result) -> Result:
        if self.state_exists:
            result = Result(success=False,
                            message="bla bla ALREADY_EXISTS bla bla", code=1)
        else:
            result = Result(success=True, message="Whatever", code=0)
        return super().after_create(result)


def test_singleton_first_creation(deployer, common_params):

    deployer.set_common_params(common_params)

    s = ServiceSingletonImmutable(state_exists=False)
    deployer.deploy(s)

    assert s.last_result.success
    assert not s.already_exists


def test_singleton_already_exists(deployer, common_params):

    deployer.set_common_params(common_params)

    s = ServiceSingletonImmutable(state_exists=True)
    deployer.deploy(s)

    assert s.last_result.success
    assert s.already_exists

# ==============================================================


class ServiceRevisionBased(GCPServiceRevisionBased):
    def params_create(self):
        return ["create", "param_create"]


def test_revision_based_normal(deployer):

    s = ServiceRevisionBased()
    deployer.deploy(s)

    assert s.last_result.success


# ==============================================================

class ServiceNotDeployable(GCPServiceRevisionBased):

    def params_create(self):
        return ["create", "param_create"]

    def after_create(self, result: Result) -> Result:
        return Result(success=False, message="Some Error", code=1)


def test_revision_based_not_deployable(deployer):

    s = ServiceNotDeployable()

    with pytest.raises(SystemExit):
        deployer.deploy(s)

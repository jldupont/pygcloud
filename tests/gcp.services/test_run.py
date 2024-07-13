"""
@author: jldupont
"""
import pytest
from pygcloud.models import Result, Param
from pygcloud.gcp.services.run import CloudRun, CloudRunNeg
from pygcloud.gcp.models import CloudRunRevisionSpec
from samples import CLOUD_RUN_REVISION_SPEC


class MockCloudRun(CloudRun):

    def after_describe(self, result):

        new_result = Result(success=True,
                            message=CLOUD_RUN_REVISION_SPEC,
                            code=0
                            )

        return super().after_describe(new_result)

    def params_create(self):
        if self.just_describe:
            raise Exception("Should only describe...")
        return super().params_create()


@pytest.fixture
def cr():
    return MockCloudRun("my-service", Param("--p1", "v1"), region="region")


def test_run_deploy(deployer, cr):

    common_params = [
        Param("--project", "my-project")
    ]

    deployer.add_common_params(common_params)

    deployer.deploy(cr)

    assert deployer.cmd.last_command_args == \
        [
            "echo", "beta", "run", "deploy",
            "my-service", "--clear-labels",
            "--region", "region",
            "--p1", "v1",
            "--project", "my-project"
        ], print(deployer.cmd.last_command_args)


def test_run_with_use(deployer, cr, sn1):

    cr.use(sn1)
    deployer.deploy(cr)

    assert deployer.cmd.last_command_args == \
        [
            "echo", "beta", "run", "deploy",
            "my-service", "--clear-labels",
            "--region", "region",
            "--p1", "v1",
            "--labels", "pygcloud-use-0=ns1--name1"
        ], print(deployer.cmd.last_command_args)


def test_cloud_run_just_describe(deployer, cr):

    cr.set_just_describe()
    deployer.deploy(cr)

    assert cr.last_result.success, print(cr.last_result)
    # if the create phase was attempted,
    # then there would be an exception raised

    assert isinstance(cr.spec, CloudRunRevisionSpec)


def test_cloud_run_neg(deployer):

    neg = CloudRunNeg("neg", [
        "--param", "value"
    ], region="region")

    deployer.deploy(neg)
    assert deployer.cmd.last_command_args == \
        [
            "echo", "beta", "compute", "network-endpoint-groups",
            "describe", "neg",
            "--region", "region",
        ], print(deployer.cmd.last_command_args)

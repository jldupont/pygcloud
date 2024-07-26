"""
@author: jldupont
"""
import pytest
from pygcloud.models import Result, Param
from pygcloud.gcp.services.run import CloudRun
from pygcloud.gcp.models import CloudRunRevisionSpec, CloudRunNegSpec
from pygcloud.gcp.services.iam import ServiceAccountCapableMixin
from samples import CLOUD_RUN_REVISION_SPEC


class MockCloudRun(CloudRun, ServiceAccountCapableMixin):

    def after_describe(self, result):

        new_result = Result(success=True,
                            message=CLOUD_RUN_REVISION_SPEC,
                            code=0
                            )

        return super().after_describe(new_result)

    def after_create(self, _):
        new_result = Result(success=True,
                            message=CLOUD_RUN_REVISION_SPEC,
                            code=0
                            )
        return super().after_create(new_result)

    def params_create(self):
        if self.just_describe:
            raise Exception("Should only describe...")
        return super().params_create()


@pytest.fixture
def cr():
    return MockCloudRun("my-service", Param("--p1", "v1"), region="region")


def test_run_deploy(deployer, mock_sg, cr):

    common_params = [
        Param("--project", "my-project")
    ]

    deployer.add_common_params(common_params)

    mock_sg.add(cr)

    deployer.deploy(mock_sg)

    assert deployer.cmd.last_command_args == \
        [
            "echo", "beta", "run", "deploy",
            "my-service", "--clear-labels",
            "--region", "region",
            "--format", "json",
            "--p1", "v1",
            "--project", "my-project",
        ], print(deployer.cmd.last_command_args)


def test_run_with_use(deployer, mock_sg, cr, sn1):

    cr.use(sn1)
    mock_sg.add(cr)

    deployer.deploy(mock_sg)

    assert deployer.cmd.last_command_args == \
        [
            "echo", "beta", "run", "deploy",
            "my-service", "--clear-labels",
            "--region", "region",
            "--format", "json",
            "--p1", "v1",
            "--labels", "pygcloud-use-0=ns1--name1",
        ], print(deployer.cmd.last_command_args)


def test_cloud_run_just_describe(deployer, mock_sg, cr):

    cr.set_just_describe()

    mock_sg + cr
    deployer.deploy(mock_sg)

    assert cr.last_result.success, print(cr.last_result)
    # if the create phase was attempted,
    # then there would be an exception raised

    assert isinstance(cr.spec, CloudRunRevisionSpec)


'''
TODO: just build a proper mock
@pytest.mark.skip
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
'''


def test_cloudrun_neg(sample_cloudrun_neg):

    n = CloudRunNegSpec.from_string(sample_cloudrun_neg)

    assert n.name == "backend-neg"

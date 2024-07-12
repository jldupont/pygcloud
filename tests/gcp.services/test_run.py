"""
@author: jldupont
"""
import pytest
from pygcloud.gcp.services.run import CloudRun, CloudRunNeg
from pygcloud.models import Param


@pytest.fixture
def cr():
    return CloudRun("my-service", Param("--p1", "v1"), region="region")


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

"""
@author: jldupont
"""
from pygcloud.gcp.services.run import CloudRun
from pygcloud.models import Param


def test_run_deploy(deployer):

    common_params = [
        Param("--project", "my-project")
    ]

    deployer.add_common_params(common_params)

    service = CloudRun("my-service", Param("--p1", "v1"))
    deployer.deploy(service)

    assert deployer.cmd.last_command_args == \
        ["echo", "beta", "run", "deploy",
            "my-service", "--p1=v1", "--project=my-project"]

"""
@author: jldupont
"""
from pygcloud.gcp.services.storage import StorageBucket


def test_gcs(deployer):

    b = StorageBucket("bucket")

    deployer.deploy(b)

    assert deployer.cmd.last_command_args == [
        "echo", "storage", "buckets", "create", "gs://bucket"
    ]

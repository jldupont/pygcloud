"""
@author: jldupont
"""
from pygcloud.gcp.services.storage import StorageBucket


def test_gcs(deployer):

    b = StorageBucket("bucket")

    deployer.deploy(b)

    # "update" because the "describe" stage will succeed

    assert deployer.cmd.last_command_args == [
        "echo", "storage", "buckets", "update", "gs://bucket"
    ]

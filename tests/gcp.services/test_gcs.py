"""
@author: jldupont
"""

from pygcloud.gcp.services.storage import StorageBucket
from pygcloud.models import Result
from samples import STORAGE_BUCKET


class MockStorageBucket(StorageBucket):

    def after_describe(self, result):
        result = Result(success=True, message=STORAGE_BUCKET, code=0)
        return super().after_describe(result)


def test_gcs(deployer, mock_sg, sample_gcs_bucket):

    b = MockStorageBucket("bucket")
    mock_sg + b

    deployer.deploy(mock_sg)

    # "update" because the "describe" stage will succeed

    assert deployer.cmd.last_command_args == [
        "echo",
        "storage",
        "buckets",
        "update",
        "gs://bucket",
        "--format",
        "json",
    ]

    assert b.spec.name == "bucket"

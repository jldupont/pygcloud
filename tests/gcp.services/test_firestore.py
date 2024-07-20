"""
@author: jldupont
"""
from pygcloud.models import Result
from pygcloud.gcp.services.firestore import FirestoreDatabase, \
    FirestoreIndexComposite
from samples import FIRESTORE_DB


class MockFirestoreDatabase(FirestoreDatabase):

    def after_describe(self, result):

        new_result = Result(success=True,
                            message=FIRESTORE_DB,
                            code=0
                            )

        return super().after_describe(new_result)

    def after_create(self, result):

        new_result = Result(success=True,
                            message=FIRESTORE_DB,
                            code=0
                            )

        return super().after_create(new_result)


def test_firestore_database_already_exists(deployer):

    d = MockFirestoreDatabase("(default)")

    deployer.deploy(d)

    assert deployer.cmd.last_command_args == [
        "echo", "firestore", "databases", "describe",
        "--database", "(default)", "--format", "json"
    ], print(deployer.cmd.last_command_args)


def test_firestore_index_composite(deployer):

    i = FirestoreIndexComposite("default")

    deployer.deploy(i)

    assert deployer.cmd.last_command_args == [
        "echo", "firestore", "indexes", "composite", "create",
        "--database", "default"
    ], print(deployer.cmd.last_command_args)

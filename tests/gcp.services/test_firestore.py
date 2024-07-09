"""@author: jldupont"""
from pygcloud.gcp.services.firestore import FirestoreDatabase, \
    FirestoreIndexComposite


def test_firestore_database_already_exists(deployer):

    d = FirestoreDatabase("default")

    deployer.deploy(d)

    assert deployer.cmd.last_command_args == [
        "echo", "firestore", "databases", "describe",
        "--database", "default"
    ], print(deployer.cmd.last_command_args)


def test_firestore_index_composite(deployer):

    i = FirestoreIndexComposite("default")

    deployer.deploy(i)

    assert deployer.cmd.last_command_args == [
        "echo", "firestore", "indexes", "composite", "create",
        "--database", "default"
    ], print(deployer.cmd.last_command_args)

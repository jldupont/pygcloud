"""@author: jldupont"""
from pygcloud.gcp.services.firestore import FirestoreDatabase


def test_firestore_database_already_exists(deployer):

    d = FirestoreDatabase("default")

    deployer.deploy(d)

    assert deployer.cmd.last_command_args == [
        "echo", "firestore", "databases", "describe",
        "--databases", "default"
    ], print(deployer.cmd.last_command_args)

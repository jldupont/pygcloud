import pytest
from pygcloud.deployer import Deployer
from pygcloud.core import CommandLine


@pytest.fixture
def cmd_echo():
    return CommandLine("echo")


@pytest.fixture
def deployer(cmd_echo):
    return Deployer(cmd_echo)

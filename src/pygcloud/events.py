"""
@author: jldupont

(
    EntryPoint(name='pygcloud_before_deploy',
        value='pygcloud.events:before_deploy', group='pygcloud.events'),
        ...
)

NOTE The package must be installed locally through `install.sh` in order
     for the testing of `entry-points` to take place.
"""

from typing import Union
from .hooks import execute_hooks_deployer
from .models import GCPService, ServiceGroup, GroupName, Result, Instruction


def dummy(_deployer_instance, *_p, **_kw):
    """For test purposes only"""


def start_deploy(deployer_instance, what: Union[GCPService, ServiceGroup, GroupName]):
    """
    Prototype of entrypoint 'start_deploy'

    Executed at the very beginning of the invocation of
    the deployment task
    """
    execute_hooks_deployer("start_deploy", deployer_instance, what)


def before_deploy(deployer_instance, service: GCPService):
    """
    Before a service deployment task is executed
    """
    execute_hooks_deployer("before_deploy", deployer_instance, service)


def after_deploy(deployer_instance, service: GCPService):
    """
    After a service deployment task has completed
    either successfully or not
    """
    execute_hooks_deployer("after_deploy", deployer_instance, service)


def end_deploy(
    deployer_instance,
    what: Union[GCPService, ServiceGroup, GroupName],
    result: Union[Result, Instruction],
):
    """
    Prototype of entrypoint 'end_deploy'

    Executed at the very end of the invocation of the
    the deployment task
    """
    execute_hooks_deployer("end_deploy", deployer_instance, what, result)

"""
@author: jldupont
"""
import logging
import sys
from .core import CommandLine, GCloud
from .models import GCPService, Result


class Deployer:

    def __init__(self, cmd: CommandLine = None, exit_on_error=True):
        """
        exit_on_error (bool): by default, applies to create
        and update operations
        """

        self.cmd = cmd or GCloud()
        self.exit_on_error = exit_on_error

    def before_deploy(self, service: GCPService): pass
    def before_create(self, service: GCPService): pass
    def before_update(self, service: GCPService): pass
    def before_delete(self, service: GCPService): pass

    def after_create(self, service: GCPService, result: Result):
        if self.exit_on_error and not result.success:
            logging.error(result.message)
            sys.exit(1)

    def after_update(self, service: GCPService, result: Result):
        if self.exit_on_error and not result.success:
            logging.error(result.message)
            sys.exit(1)

    def after_delete(self, service: GCPService, result: Result): pass
    def after_deploy(self, service: GCPService, result: Result): pass

    def deploy(self, service: GCPService):

        self.before_deploy(service)

        #
        # Phase 1: Description
        #
        service.before_describe()
        describe_params = service.params_describe()
        result = self.cmd.exec(describe_params)
        service.after_describe(result)

        # Phase 2: Either create or update

        if service.already_exists:
            result = self.update(service)
        else:
            result = self.create(service)

        self.after_deploy(service, result)
        return result

    def create(self, service: GCPService) -> Result:

        self.before_create(service)
        service.before_create()
        params = service.params_create()
        result = self.cmd.exec(params)
        self.after_create(service, result)
        service.after_create(result)
        return result

    def update(self, service: GCPService) -> Result:

        self.before_update(service)
        service.before_update()
        params = service.params_update()
        result = self.cmd.exec(params)
        self.after_update(service, result)
        service.after_update(result)
        return result

    def delete(self, service: GCPService) -> Result:

        self.before_delete(service)
        service.before_delete()
        params = service.params_delete()
        result = self.cmd.exec(params)
        self.after_delete(service, result)
        service.after_delete(result)
        return result

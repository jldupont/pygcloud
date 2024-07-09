"""
@author: jldupont
"""
import logging
import sys
from .core import CommandLine, GCloud
from .models import GCPService, Result, Params
from .constants import ServiceCategory

logger = logging.getLogger("pygcloud.deployer")


class Deployer:

    def __init__(self, cmd: CommandLine = None, exit_on_error=True,
                 log_error=True,
                 common_params: Params = None):
        """
        exit_on_error (bool): by default, applies to create
        and update operations
        """
        self.cmd = cmd or GCloud()
        self.exit_on_error = exit_on_error
        self.log_error = log_error
        self.common_params = common_params or []

    @property
    def command(self):
        return self.cmd

    def set_common_params(self, params: Params):
        assert isinstance(params, list)
        self.common_params = params
        return self

    def add_common_params(self, params: Params):
        assert isinstance(params, list)
        self.common_params.extend(params)
        return self

    def before_describe(self, service: GCPService): pass

    def before_deploy(self, service: GCPService):
        logger.info(f"Before deploying {service.ns}:{service.name}")

    def before_create(self, service: GCPService): pass
    def before_update(self, service: GCPService): pass
    def before_delete(self, service: GCPService): pass

    def after_describe(self, service: GCPService, result: Result): pass
    def after_deploy(self, service: GCPService, result: Result): pass

    def after_create(self, service: GCPService, result: Result):
        if result is None:
            raise Exception("Expecting a valid Result")

        if self.exit_on_error and not result.success:
            if self.log_error:
                logger.error(result.message)
            sys.exit(1)

    def after_update(self, service: GCPService, result: Result):
        if result is None:
            raise Exception("Expecting a valid Result")

        if self.exit_on_error and not result.success:
            if self.log_error:
                logger.error(result.message)
            sys.exit(1)

    def after_delete(self, service: GCPService, result: Result): pass

    def describe(self, service: GCPService) -> Result:

        self.before_describe(service)
        service.before_describe()
        params = service.params_describe()
        result = self.cmd.exec(params, common=self.common_params)
        service.after_describe(result)
        self.after_describe(service, result)
        return result

    def deploy_singleton_immutable(self, service: GCPService) -> Result:
        """
        We ignore exceptions arising from the service already being created.
        The service's "after_create" method will need to check for this.
        """
        self.before_deploy(service)

        if service.REQUIRES_DESCRIBE_BEFORE_CREATE:
            self.describe(service)

            if service.already_exists:
                self.after_deploy(service, service.last_result)
                return service.last_result

        self.create(service)

        result = self.create(service)
        return self.after_deploy(service, result)

    def deploy_revision_based(self, service: GCPService) -> Result:
        """
        We skip the "update" step. The "create" parameters will be used.
        The "SingletonImmutable" and "RevisionBased" categories are
        indistinguishable from the Deployer point of view: the logic to
        handle them is located in the Service class.
        """
        self.before_deploy(service)
        result = self.create(service)
        return self.after_deploy(service, result)

    def deploy_updateable(self, service: GCPService) -> Result:
        """
        We do the complete steps i.e. describe, create or update.
        """
        self.before_deploy(service)
        self.describe(service)

        if service.already_exists:
            result = self.update(service)
        else:
            result = self.create(service)

        self.after_deploy(service, result)
        return result

    def deploy(self, service: GCPService) -> Result:

        # The "match" statement is only available from Python 3.10 onwards
        # https://docs.python.org/3/whatsnew/3.10.html#match-statements
        if service.category == ServiceCategory.SINGLETON_IMMUTABLE:
            return self.deploy_singleton_immutable(service)

        if service.category == ServiceCategory.REVISION_BASED:
            return self.deploy_revision_based(service)

        if service.category == ServiceCategory.UPDATABLE:
            return self.deploy_updateable(service)

        raise RuntimeError(f"Unknown service category: {service.category}")

    def create(self, service: GCPService) -> Result:

        self.before_create(service)
        service.before_create()
        params = service.params_create()
        result = self.cmd.exec(params, common=self.common_params)
        result = service.after_create(result)
        self.after_create(service, result)

        if service.REQUIRES_UPDATE_AFTER_CREATE:
            result = self.update(service)

        return result

    def update(self, service: GCPService) -> Result:

        self.before_update(service)
        service.before_update()
        params = service.params_update()
        result = self.cmd.exec(params, common=self.common_params)
        result = service.after_update(result)
        self.after_update(service, result)
        return result

    def delete(self, service: GCPService) -> Result:

        self.before_delete(service)
        service.before_delete()
        params = service.params_delete()
        result = self.cmd.exec(params, common=self.common_params)
        result = service.after_delete(result)
        self.after_delete(service, result)
        return result

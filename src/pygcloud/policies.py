"""
@author: jldupont
"""
from pygcloud.models import Policy, PolicyViolation
from pygcloud.models import ServiceGroups, GCPService
from pygcloud.gcp.services.iam import ServiceAccountCapableMixin


class PolicyServiceAccount(Policy):
    """
    Services should have a non-default Service Account
    """

    @classmethod
    def evaluate(cls, groups: ServiceGroups, service: GCPService):

        if isinstance(service, ServiceAccountCapableMixin):
            if service.service_account is None:
                raise PolicyViolation("Service can and should be provisioned "
                                      "with a non-default Service Account")


class PolicyProjectLevelBindings(Policy):
    """
    Prohibit the usage of IAM bindings from outside
    of the service's project
    """

    @classmethod
    def evaluate(cls, groups: ServiceGroups, service: GCPService):
        ...


class PolicyIngress(Policy):
    """
    A service
    """

    @classmethod
    def evaluate(cls, groups: ServiceGroups, service: GCPService):
        ...

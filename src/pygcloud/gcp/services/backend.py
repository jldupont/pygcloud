"""
@author: jldupont
"""
import logging
from pygcloud.models import GCPServiceSingletonImmutable, Result, Params


class BackendService(GCPServiceSingletonImmutable):
    """
    Backend services accessible external load balancers

    https://cloud.google.com/sdk/gcloud/reference/compute/backend-services
    """
    REQUIRES_DESCRIBE_BEFORE_CREATE = True

    def __init__(self, name: str, *params: Params):
        super().__init__(name=name, ns="be")
        self._params = params

    def params_describe(self):
        return [
            "compute", "backend-services", "describe", self.name,
        ] + self._params

    def after_describe(self, result: Result) -> Result:
        self.already_exists = result.success
        return result

    def params_create(self):
        return [
            "compute", "backend-services", "create", self.name
        ] + self._params

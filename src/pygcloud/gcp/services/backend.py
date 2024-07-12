"""
@author: jldupont
"""
from pygcloud.models import GCPServiceSingletonImmutable, Result, Params


class BackendService(GCPServiceSingletonImmutable):
    """
    Backend services accessible external load balancers

    https://cloud.google.com/sdk/gcloud/reference/compute/backend-services
    """
    REQUIRES_DESCRIBE_BEFORE_CREATE = True

    def __init__(self, name: str, params_describe: Params,
                 params_create: Params):
        super().__init__(name=name, ns="be")
        self._params_describe = params_describe
        self._params_create = params_create

    def params_describe(self):
        return [
            "compute", "backend-services", "describe", self.name,
        ] + self._params_describe

    def after_describe(self, result: Result) -> Result:
        self.already_exists = result.success
        return result

    def params_create(self):
        return [
            "compute", "backend-services", "create", self.name
        ] + self._params_create

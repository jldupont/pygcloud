"""
@author: jldupont
"""
import logging
from pygcloud.models import GCPServiceSingletonImmutable, Result
from pygcloud.gcp.models import IPAddress


class ServicesAddress(GCPServiceSingletonImmutable):
    """
    For creating the IP address

    https://cloud.google.com/sdk/gcloud/reference/compute/addresses
    """
    REQUIRES_DESCRIBE_BEFORE_CREATE = True

    def __init__(self, name: str):
        super().__init__(name=name, ns="ip")
        self._address = None

    @property
    def address(self):
        return self._address

    def params_describe(self):
        return [
            "compute", "addresses", "describe", self.name,
            "--global", "--format", "json"
        ]

    def _init_with_json(self, json_str: str):
        try:
            self._address = IPAddress.from_json_string(json_str)
        except Exception:
            raise ValueError("Cannot parse for IP address: "
                             f"{json_str}")

    def after_describe(self, result: Result) -> Result:

        if not result.success:
            self.already_exists = False
            return result

        self.already_exists = True
        self._init_with_json(result.message)

        return result

    def params_create(self):
        return [
            "compute", "addresses", "create", self.name,
            "--ip-version=IPv4", "--global",
            "--network-tier", "PREMIUM",
            "--format", "json"
        ]

    def after_create(self, result: Result) -> Result:

        if not result.success:
            # will get handled by Deployer
            return result

        self._init_with_json(result.message)

        logging.debug(f"IP address created: {self._address}")

        return result

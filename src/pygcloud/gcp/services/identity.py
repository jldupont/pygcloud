"""
Services Identity

@author: jldupont
"""
from pygcloud.models import GCPServiceSingletonImmutable


class ServicesIdentityIAP(GCPServiceSingletonImmutable):
    """
    For creating the IAP service account

    https://cloud.google.com/sdk/gcloud/reference/beta/identity
    """

    def params_create(self):
        return [
            "beta", "services", "identity", "create",
            "--service", "iap,googleapis.com",
            "--format", "json"
        ]

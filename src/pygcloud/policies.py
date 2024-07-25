"""
@author: jldupont
"""
from pygcloud.models import Policy


class PolicyServiceAccount(Policy):
    """
    Services should have a non-default Service Account

    Go through all ServiceGroup to identify services
    that have the option to use a service account other
    than the default assigned by GCP
    """


class PolicyX(Policy):
    """
    """

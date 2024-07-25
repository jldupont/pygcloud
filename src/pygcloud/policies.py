"""
@author: jldupont
"""
from pygcloud.models import Policy


class PolicyServiceAccount(Policy):
    """
    Services should have a non-default Service Account
    """

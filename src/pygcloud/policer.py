"""
Policer

@author: jldupont
"""
import logging
import sys
from typing import List
from .models import Policy, PolicyViolation
from .models import service_groups, ServiceGroup, GCPService


warn = logging.warning
error = logging.error


class _Policer:

    def __init__(self):
        self._disabled: List[Policy] = []

    def _eval_one(self, policy: Policy, service: GCPService):

        try:
            policy.eval(service_groups, service)

        except PolicyViolation as e:

            if policy in self._disabled:
                warn(f"Disabled '{policy.name}' raised"
                     f" violation but ignoring: {e}")
                return

            raise

        except Exception as e:

            if policy in self._disabled:
                warn(f"Disabled '{policy.name}' raised: {e}")
                return

            error(f"Policy 'name' raised: {e}")
            sys.exit(1)

    def _process_one(self, policy: Policy):
        """
        Go through all service groups so that each service
        is verified against the policy.

        The `eval` method is also given access to all
        service groups to account for more complex patterns.
        """

        group: ServiceGroup
        service: GCPService

        for group in service_groups:
            for service in group:
                if policy.allows(service):
                    warn(f"Policy '{policy.name}' allows "
                         f"service '{service.name}'. Skipping.")
                    continue
                self._eval_one(policy, service)

    def police(self):

        _all: List[Policy] = Policy.derived_classes

        policy: Policy

        for policy in _all:
            self._process_one(policy)

    def disable(self, policy: Policy):
        assert isinstance(policy, Policy)
        self._disabled.append(policy)


# Singleton instance
Policer = _Policer()

"""
Policer

@author: jldupont
"""
import logging
import sys
from typing import List
from .models import Policy, PolicyViolation
from .models import service_groups


warn = logging.warning
error = logging.error


class _Policer:

    def __init__(self):
        self._disabled = []

    def _process_one(self, policy: Policy):
        name = policy.__class__.__name__

        try:
            policy.eval()

        except PolicyViolation as e:

            if policy in self._disabled:
                warn(f"Disabled '{name}' raised violation but ignoring: {e}")
                return

            raise

        except Exception as e:

            if policy in self._disabled:
                warn(f"Disabled '{name}' raised: {e}")
                return

            error(f"Policy 'name' raised: {e}")
            sys.exit(1)

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

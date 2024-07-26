"""
@author: jldupont
"""
import pytest
from typing import List
from pygcloud.models import Policy, ServiceGroup, GCPService, PolicyViolation
from pygcloud.policer import Policer, PolicingResults, PolicingResult
from pygcloud.policies import PolicyServiceAccount
from pygcloud.gcp.services.iam import ServiceAccountCapableMixin
from pygcloud.constants import PolicerMode


class MockPolicy(Policy):

    @classmethod
    def evaluate(cls, groups: List[ServiceGroup], service: GCPService):
        ...


class MockServiceSupportingServiceAccount(GCPService, ServiceAccountCapableMixin):
    ...


@pytest.fixture
def mock_policy():
    return MockPolicy


def test_policy_derived_classes(mock_policy):

    assert isinstance(Policy.derived_classes, list), \
        print(Policy.derived_classes)

    assert PolicyServiceAccount in Policy.derived_classes
    assert Policy not in Policy.derived_classes


def test_policy_allowed(mock_policy, mock_service):

    mock_policy.allow(mock_service, "some reason")

    assert mock_policy.allows(mock_service)


def test_policy_should_have_service_account(mock_sg):

    Policer.mode = PolicerMode.DRY_RUN

    mock_service = MockServiceSupportingServiceAccount()
    # no service account added

    mock_sg.clear()
    mock_sg + mock_service

    results: PolicingResults = Policer.police()

    policy_violated_result: PolicingResult = results.outcome
    policy_class_violated: Policy = policy_violated_result.policy

    assert policy_class_violated is PolicyServiceAccount, \
        print(results)

    Policer.mode = PolicerMode.RUN

    with pytest.raises(PolicyViolation):
        Policer.police()

"""
@author: jldupont
"""
import pytest
from pygcloud.models import Policy
from pygcloud.policies import PolicyServiceAccount


class MockPolicy(Policy):
    ...


@pytest.fixture
def mock_policy():
    return MockPolicy()


def test_policy_derived_classes(mock_policy):

    assert isinstance(Policy.derived_classes, list), \
        print(Policy.derived_classes)

    assert PolicyServiceAccount in Policy.derived_classes
    assert Policy not in Policy.derived_classes

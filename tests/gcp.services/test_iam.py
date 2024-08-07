"""
@author: jldupont
"""

import pytest
from pygcloud.models import Result
from pygcloud.gcp.models import IAMBinding, IAMBindings, IAMPolicy, IAMMember
from pygcloud.gcp.services.iam import IAMBindingService, ServiceAccount
from pygcloud.gcp.services.run import CloudRun
from pygcloud.gcp.services.projects import ProjectIAMBindingService
from samples import PROJECT_BINDINGS


@pytest.fixture
def mock_bidon_binding():
    return IAMBinding(email="ns:whatever_email", role="whatever_role")


class MockCR(CloudRun): ...  # NOQA


class MockProjectIAMBindingService(ProjectIAMBindingService):

    def after_describe(self, result: Result):
        new_result = Result(success=True, message=PROJECT_BINDINGS, code=0)
        return super().after_describe(new_result)

    def after_create(self, result: Result):
        new_result = Result(success=True, message=PROJECT_BINDINGS, code=0)
        return super().after_create(new_result)


class MockIAMBindingService(IAMBindingService):

    def params_describe(self):
        params = super().params_describe()

        setattr(self, "captured_describe_params", params)
        return params

    def params_create(self):
        params = super().params_create()

        setattr(self, "captured_create_params", params)
        return params

    def after_describe(self, result: Result):
        new_result = Result(success=True, message=PROJECT_BINDINGS, code=0)
        return super().after_describe(new_result)

    def after_create(self, result: Result):
        new_result = Result(success=True, message=PROJECT_BINDINGS, code=0)
        return super().after_create(new_result)


def test_project_bindings_does_not_exists(deployer, mock_sg, mock_bidon_binding):

    service = MockProjectIAMBindingService(mock_bidon_binding, "project_id")

    mock_sg.clear()

    mock_sg + service

    deployer.deploy(mock_sg)

    assert not service.already_exists


def test_project_bindings_already_exists(deployer, mock_sg):

    policy: IAMPolicy = IAMPolicy.from_json_list(PROJECT_BINDINGS)

    first_binding: IAMBindings = policy.bindings[0]
    first_member: IAMMember = first_binding.members[0]

    b = IAMBinding(
        ns=first_member.ns, email=first_member.email, role=first_binding.role
    )

    service = MockProjectIAMBindingService(b, "project_id")

    mock_sg.clear()

    mock_sg + service

    deployer.deploy(mock_sg)

    assert service.already_exists


def test_iam_binding_service(deployer, mock_sg, mock_bidon_binding):

    cr = MockCR("cr_srv", region="some_region")

    srv = MockIAMBindingService(cr, mock_bidon_binding)

    mock_sg + srv

    deployer.deploy(mock_sg)

    assert not srv.already_exists

    assert srv.captured_describe_params == [
        ["beta", "run"],
        ["services"],
        "get-iam-policy",
        "cr_srv",
        "--format",
        "json",
        ["--region", "some_region"],
        [],
    ], print(srv.captured_describe_params)

    assert srv.captured_create_params == [
        ["beta", "run"],
        ["services"],
        "add-iam-policy-binding",
        "cr_srv",
        "--member",
        "ns:whatever_email",
        "--role",
        "whatever_role",
        "--format",
        "json",
        ["--region", "some_region"],
        [],
    ], print(srv.captured_create_params)


def test_service_account():

    sa = ServiceAccount("sa_name", "project_id")
    assert "@" in sa.name and "project_id" in sa.name
    assert sa.id == "sa_name"

"""
@author: jldupont
"""


def test_service_account_iam_already_exists(
                             deployer,
                             mock_service_account_iam_class,
                             sample_binding):

    service = mock_service_account_iam_class(sample_binding,
                                             project_id="xyz")

    result = deployer.deploy(service)

    assert service.before_describe_called
    assert not service.after_created_called, print(result)


def test_service_account_iam_non_existent_binding(
    deployer,
    sample_fake_binding,
    mock_service_account_iam_class
):
    service = mock_service_account_iam_class(sample_fake_binding,
                                             project_id="xyz")

    result = deployer.deploy(service)

    assert service.after_created_called
    assert result.success

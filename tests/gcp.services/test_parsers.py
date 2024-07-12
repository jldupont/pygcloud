"""
@author: jldupont
"""
from pygcloud.gcp.parsers import IAMBindings, IAMBinding


def test_iam_binding():

    b = IAMBinding(email="ns:email", role="role", ns=...)

    assert b.email == "email"
    assert b.role == "role"
    assert b.ns == "ns"


def test_project_bindings(project_bindings):

    b = project_bindings.bindings

    assert len(b) == 15

    first = b[0]
    assert first.role == "roles/artifactregistry.serviceAgent"


def test_project_bindings_itemize(project_bindings):

    bindings = project_bindings.bindings
    first_binding = bindings[0]
    assert isinstance(first_binding, IAMBindings)
    assert first_binding.members == \
        ["serviceAccount:service-215695389495"
         "@gcp-sa-artifactregistry.iam.gserviceaccount.com"]

    items = project_bindings._itemize(first_binding)
    assert len(items) == 1

    first_item = items[0]
    assert isinstance(first_item, IAMBinding)
    assert first_item.role == "roles/artifactregistry.serviceAgent"

    all_bindings = project_bindings.items

    assert len(all_bindings) == 18


def test_project_bindings_find_member_entries(project_bindings):

    sa = "280761648870@cloudbuild.gserviceaccount.com"
    result = project_bindings.find_bindings_by_member_email(sa)
    assert isinstance(result, list)

    print(project_bindings.items)
    assert len(result) == 4, print(result)


def test_project_bindings_find_members_for_role(project_bindings):

    role = "roles/editor"
    result = project_bindings.find_bindings_for_role(role)

    assert len(result) == 3


def test_project_bindings_check_for_target_binding(project_bindings,
                                                   sample_binding):

    assert project_bindings.\
        check_for_target_binding(sample_binding)

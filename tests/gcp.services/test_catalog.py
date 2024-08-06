"""
@author: jldupont
"""

from pygcloud.models import GCPService, GCPServiceUnknown
from pygcloud.gcp.models import ServiceDescription, Ref
from pygcloud.gcp.services.addresses import ServicesAddress
from pygcloud.gcp.services.iam import ServiceAccount
from pygcloud.gcp.catalog import (
    ServiceNode,
    lookup,
    get_listable_services,
    get_service_classes_from_services_list,
    lookup_service_class_from_ref,
)

COUNT_TOTAL = 22
COUNT_LISTABLE = 14
COUNT_LISTABLE_ENABLED_IN_SAMPLE = 13


def test_catalog():
    a = ServiceNode.__all_classes__
    assert len(a) >= COUNT_TOTAL, print("Have you updated the catalog?")


def test_lookup():
    classe = lookup("FirestoreDatabase")
    assert issubclass(classe, GCPService), print(type(classe))


def test_lookup2():
    classe = lookup("ServiceAccount")
    assert issubclass(classe, GCPService), print(classe)


def test_listable():

    assert len(get_listable_services()) >= COUNT_LISTABLE, print(
        get_listable_services()
    )


def test_listable_enabled(sample_services_list):

    liste = ServiceDescription.from_json_list(sample_services_list)

    result = get_service_classes_from_services_list(liste)

    assert len(result) >= COUNT_LISTABLE_ENABLED_IN_SAMPLE, print(result)

    first = result[0]

    assert issubclass(first, GCPService)


def test_catalog_lookup_service_class_from_ref():

    r = Ref(
        project="PROJECT", region="REGION", service_type="addresses", name="whatever"
    )

    result: GCPService = lookup_service_class_from_ref(r)
    assert result == ServicesAddress


def test_catalog_lookup_service_class_from_ref_unknown():

    r = Ref(project="PROJECT", region="REGION", service_type="unknown", name="whatever")

    result: GCPService = lookup_service_class_from_ref(r)
    assert result == GCPServiceUnknown


def test_lookup_service_class_from_ref2():

    r = Ref(project="PROJECT",
            region="REGION",
            service_type=ServiceAccount,
            name="projects/PROJECT/serviceAccounts/215695389495-compute@developer.gserviceaccount.com")

    result: GCPService = lookup_service_class_from_ref(r)
    assert result == ServiceAccount, print(result)

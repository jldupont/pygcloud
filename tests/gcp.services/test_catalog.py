"""
@author: jldupont
"""
from pygcloud.models import GCPService
from pygcloud.gcp.models import ServiceDescription
from pygcloud.gcp.catalog import ServiceNode, lookup, \
    get_listable_services, get_service_classes_from_services_list

COUNT_TOTAL = 20
COUNT_LISTABLE = 13
COUNT_LISTABLE_ENABLED_IN_SAMPLE = 12


def test_catalog():
    a = ServiceNode.__all_classes__
    assert len(a) == COUNT_TOTAL, print("Have you updated the catalog?")


def test_lookup():
    classe = lookup("FirestoreDatabase")
    assert issubclass(classe, GCPService), print(type(classe))


def test_listable():

    assert len(get_listable_services()) == COUNT_LISTABLE, \
        print(get_listable_services())


def test_listable_enabled(sample_services_list):

    liste = ServiceDescription.from_json_list(sample_services_list)

    result = get_service_classes_from_services_list(liste)

    assert len(result) == COUNT_LISTABLE_ENABLED_IN_SAMPLE, \
        print(result)

    first = result[0]

    assert issubclass(first, GCPService)

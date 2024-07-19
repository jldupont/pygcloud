"""
@author: jldupont
"""
from pygcloud.models import GCPService
from pygcloud.gcp.catalog import ServiceNode, lookup


def test_catalog():
    a = ServiceNode.__all_classes__
    assert len(a) == 20, print("Have you updated the catalog?")


def test_lookup():
    classe = lookup("FirestoreDatabase")
    assert issubclass(classe, GCPService), print(type(classe))

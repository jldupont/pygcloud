"""
@author: jldupont
"""
from pygcloud.gcp.services import *  # NOQA
from pygcloud.models import ServiceNode


def test_catalog():

    a = ServiceNode.__all_classes__

    assert len(a) == 18, print("Have you updated the catalog?")

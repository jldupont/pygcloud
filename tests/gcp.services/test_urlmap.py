"""
@author: jldupont
"""
import pytest
from pygcloud.models import Result, service_groups
from pygcloud.gcp.models import Ref, RefSelfLink
from pygcloud.graph_models import Node
from pygcloud.gcp.services.urlmap import UrlMapDefaultService, UrlMap
from pygcloud.gcp.catalog import lookup_service_class_from_ref


@pytest.fixture
def gen_mock_service(sample_url_map_spec):

    class MockUrlMapDefaultService(UrlMapDefaultService):

        def after_describe(self, result: Result):
            new_result = Result(
                success=True,
                message=sample_url_map_spec,
                code=0)

            return super().after_describe(new_result)

    return MockUrlMapDefaultService


def test_url_map(deployer, gen_mock_service):

    service_groups.clear()
    Ref.clear()
    Node.clear()

    s = gen_mock_service("mock_url_service", "mock_default_service")

    mock_sg = service_groups.create(name="mock_sg")
    mock_sg + s

    deployer.set_just_describe()
    deployer.deploy(mock_sg)

    assert s.last_result is not None, print(s.last_result)
    assert len(Ref.all) == 1, print(Ref.all)

    ref = Ref.all[0]
    assert isinstance(ref, RefSelfLink), print(ref)

    classe = lookup_service_class_from_ref(ref)
    assert isinstance(classe, UrlMap), print(classe)


def test_build_url_map_ref_from_link():

    link = "https://www.googleapis.com/compute/v1/projects/PROJECT/global/urlMaps/urlmap-backend-service"

    ref = Ref.from_link(link)
    assert ref.service_type == "urlMaps"


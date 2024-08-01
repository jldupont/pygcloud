"""
Support for the management of diverse references
occuring in service specifications

@author: jldupont
"""

from typing import List, Union
from pygcloud.models import GCPService, Spec
from pygcloud.gcp.models import Ref
from pygcloud.graph_models import Node, Edge, Relation, Group


GraphEntities = List[Union[Node, Edge, Group]]


def process_refs(service: GCPService) -> GraphEntities:
    assert isinstance(service, GCPService)

    entities = []

    spec: Spec = service.spec

    if spec is None:
        return entities

    batch = _process_selflinks(service, spec)
    entities.extend(batch)

    batch = _process_users(service, spec)
    entities.extend(batch)

    return entities


def _process_selflinks(service: GCPService, spec: Spec) -> GraphEntities:

    nodes = []

    selfLink = getattr(spec, "selfLink", None)

    if selfLink is not None:
        nodes.append(
            Node.create_or_get(name=selfLink, kind=service.__class__, obj=service)
        )

    return nodes


def _process_users(service: GCPService, spec: Spec) -> GraphEntities:
    """
    Supports:
    * IPAddress
    """
    nodes = []

    users = getattr(service.spec, "users", [])

    for user_string_ref in users:
        ref = Ref.from_link(user_string_ref)

    return nodes

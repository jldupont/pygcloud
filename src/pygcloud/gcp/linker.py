"""
@author: jldupont
"""

from typing import Union
from pygcloud.hooks import Hooks
from pygcloud.models import GCPService, ServiceGroup, GroupName, Result, GCPUnknownService
from pygcloud.gcp.models import Ref
from pygcloud.graph_models import Node, Relation, Edge, Group, ServiceNodeUnknown
from pygcloud.gcp.catalog import lookup_service_class_from_ref


class _Linker:
    """
    The Linker awaits for all Refs at the end of a deployment
    and builds the associated Nodes and Edges

    The first step is to resolve all Nodes.
    Once all the Nodes are available for linking,
    build the edges between them

    NOTE The Node, Edge and Group classes collect their instances automatically
    """
    __instance = None

    def __init__(self):
        if self.__instance is not None:
            raise Exception("Singleton class")
        self.__instance = self
        Hooks.register_callback("end_deploy", self.end_deploy)

    def _build_nodes(self):

        all_refs = Ref.all_instances

        target: GCPService
        ref: Ref

        for ref in all_refs:
            target = lookup_service_class_from_ref(ref)

            if target == GCPUnknownService:
                # ref.service_type is unknown
                un = ServiceNodeUnknown(name=ref.service_type)
                Node.create_or_get(name=ref.name, kind=ServiceNodeUnknown, obj=un)
                continue

            Node.create_or_get(
                name=ref.name, kind=target.__class__, obj=target
            )

    def _build_edges(self):
        ...

    def end_deploy(self, _deployer,
                   _what: Union[ServiceGroup, GroupName],
                   _result: Result):
        """Called after the deployment of all services"""
        self._build_nodes()
        self._build_edges()


Linker = _Linker()

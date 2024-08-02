"""
@author: jldupont
"""

from typing import Union
from pygcloud.hooks import Hooks
from pygcloud.models import GCPService, ServiceGroup, GroupName, Result, \
    GCPServiceUnknown, GCPServiceInstanceNotAvailable
from pygcloud.gcp.models import Ref, RefUses, RefUsedBy, RefSelfLink
from pygcloud.graph_models import Node, Relation, Edge, ServiceNodeUnknown
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
        Hooks.register_callback("start_deploy", self.start_deploy)
        Hooks.register_callback("end_deploy", self.end_deploy)

    def start_deploy(self, *p):
        Ref.clear()
        Node.clear()
        Edge.clear()

    def _build_self(self, ref: Ref, service: GCPService):
        """
        Build a selfLink node
        """
        Node.create_or_get(
            name=ref.name,
            kind=service.__class__,
            obj=service
        )

    def _build_link(self, ref: Ref, source: Node, target: GCPService):

        if target == GCPServiceUnknown:
            # ref.service_type is unknown
            un = ServiceNodeUnknown(name=ref.service_type)
            Node.create_or_get(name=ref.name, kind=ServiceNodeUnknown, obj=un)
            return

        obj = target
        if target is None:
            # The service instance might not be available
            # because it is deployed / described
            obj = GCPServiceInstanceNotAvailable(ref.name, ns="n/a")

        dest: None = Node.create_or_get(
            name=ref.name,
            kind=obj.__class__,
            obj=obj
        )

        self._build_edge(ref, source, dest)

    def _build_nodes(self):
        """
        A Ref contains the "origin" (one end of a Relation)
        whilst 'service_type' and 'name' identify the other
        end of the relation
        """
        all_refs = Ref.all_instances

        target: GCPService
        ref: Ref

        for ref in all_refs:
            target = lookup_service_class_from_ref(ref)

            if isinstance(ref, RefSelfLink):
                self._build_self(ref, target)
                continue

            if ref.origin_service is None:
                raise Exception("A non selfLink reference without "
                                f"a service instance is invalid: {ref}")

            source: Node = Node.create_or_get(
                name=ref.name,
                kind=ref.origin_service.__class__,
                obj=ref.origin_service
            )

            self._build_link(ref, source, target)

    def _build_edge(self, ref: Ref, node_src: Node, node_target: Node):
        """
        From a given Node we should be able to locate
        """
        assert isinstance(ref, Ref), print(ref)
        assert isinstance(node_src, Node), print(node_src)
        assert isinstance(node_target, Node), print(node_target)

        relation: Relation = None

        if isinstance(ref, RefUses):
            relation = Relation.USES

        if isinstance(ref, RefUsedBy):
            relation = Relation.USED_BY

        Edge.create_or_get(
            relation=relation,
            source=node_src,
            target=node_target
        )

    def end_deploy(self, _deployer,
                   _what: Union[ServiceGroup, GroupName],
                   _result: Result):
        """Called after the deployment of all services"""
        self._build_nodes()


Linker = _Linker()

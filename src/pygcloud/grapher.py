"""
# Graph module

@author: jldupont
"""
import logging
from typing import Type, Dict
from .models import ServiceNode, service_groups, ServiceGroup, GCPService
from .graph_models import Relation, Edge, Node, Group
from .hooks import Hooks

try:
    import graphviz  # NOQA
    GRAPHVIZ_AVAILABLE = True
except:  # NOQA
    GRAPHVIZ_AVAILABLE = False


debug = logging.debug
info = logging.info
warning = logging.warning


class _Grapher:
    """
    Responsible for generating the service graph

    Nodes and Edges are automatically collected in their
    respective classes thanks to the BaseType metaclass
    """

    __instance = None

    def __init__(self):
        if self.__instance is not None:
            raise Exception("Singleton class")
        self.__instance = self
        Hooks.register_callback("end_linker", self.end_linker)

    def end_linker(self):
        """
        Called after the Linker has finished

        The graph entities are available in Group, Node and Edge classes
        """
        if not GRAPHVIZ_AVAILABLE:
            warning("Grapher module loaded but graphviz python package is not available")
            return

        self._build_dot()

    def _build_dot(self):
        ...


Grapher = _Grapher()

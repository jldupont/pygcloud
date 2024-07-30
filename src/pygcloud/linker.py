"""
@author: jldupont
"""
from .hooks import Hooks
from .models import Result, GCPService
from .gcp.models import LinksMap


class _Linker:

    __instance = None

    def __init__(self):
        if self.__instance is not None:
            raise Exception("Only one instance of Linker required")
        self.__instance = self
        Hooks.register_callback("after_deploy", self.after_deploy)
        Hooks.register_callback("end_deploy", self.end_deploy)

    def after_deploy(self, deployer, service: GCPService):
        """
        * Collects `selfLink`
        
        NOTE LinksMap silently ignore None keys and respects idempotency
        """
        if service.spec is not None:
            selfLink = getattr(service.spec, "selfLink", None)
            Links[selfLink] = service

    def end_deploy(self, deployer, what, result: Result):
        ...


Links = LinksMap()
Linker = _Linker()

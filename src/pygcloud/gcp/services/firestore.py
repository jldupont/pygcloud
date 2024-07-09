"""
@author: jldupont
"""
from pygcloud.models import Params, GCPServiceSingletonImmutable


class FirestoreDatabase(GCPServiceSingletonImmutable):

    REQUIRES_DESCRIBE_BEFORE_CREATE = True

    def __init__(self, name: str, params_create: Params = []):
        super().__init__(name=name, ns="fs")
        self._params_create = params_create

    def params_describe(self):
        return [
            "firestore", "databases", "describe",
            "--databases", self.name
        ]

    def params_create(self):
        return [
            "firestore", "databases", "create",
            "--databases", self.name
        ] + self._params_create

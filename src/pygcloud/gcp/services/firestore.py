"""
@author: jldupont
"""
from pygcloud.models import Params, GCPServiceSingletonImmutable


class FirestoreDatabase(GCPServiceSingletonImmutable):

    REQUIRES_DESCRIBE_BEFORE_CREATE = True

    def __init__(self, name: str, params_create: Params = []):
        super().__init__(name=name, ns="fs-db")
        self._params_create = params_create

    def params_describe(self):
        return [
            "firestore", "databases", "describe",
            "--database", self.name
        ]

    def params_create(self):
        return [
            "firestore", "databases", "create",
            "--database", self.name
        ] + self._params_create


class FirestoreIndexComposite(GCPServiceSingletonImmutable):
    """
    Cannot describe an index unfortunately
    """

    def __init__(self, db_name: str, params_create: Params = []):
        super().__init__(name=None, ns="fs-index")
        self.db_name = db_name
        self._params_create = params_create

    def params_create(self):
        return [
            "firestore", "indexes", "composite", "create",
            "--database", self.db_name
        ] + self._params_create

"""
@author: jldupont
"""
from typing import List
from pygcloud.models import Label


class LabelGenerator:
    """
    Mixin to generate labels for services
    """

    def compute_use_entries(self) -> List[Label]:
        index = 0
        tuples = []
        for use in self.uses:
            tuples.append((f"pygcloud-use-{index}", f"{use.ns}--{use.name}"))
            index += 1

        return tuples

    def generate_string_from_labels(self, labels: List[Label]) -> str:
        return ",".join([f"{key}={value}" for key, value in labels])

    def generate_use_labels(self, param_prefix="--labels"):
        """
        Builds a list of labels for the service
        based on the "use" relationships.

        The management of labels (i.e. computing adds/removes)
        is not performed here.
        """
        if len(self.uses) == 0:
            return []

        labels: List[Label] = self.compute_use_entries()
        string_ = self.generate_string_from_labels(labels)

        return [
            f"{param_prefix}", string_
        ]

"""
@author: jldupont
"""
import json
from typing import List, Any, Tuple, Union
from .models import Param


def flatten(*liste: Union[List[Any], Tuple[Any]]):
    """
    Flatten a list of lists
    """
    assert isinstance(liste, tuple), \
        f"Expected list, got: {type(liste)}"

    result = []
    for item in liste:
        if isinstance(item, list):
            result.extend(flatten(*item))
        else:
            result.append(item)
    return result


def split_head_tail(liste) -> Tuple[List[Any], List[Any]]:
    """
    Cases:
    1) head ... tail ---> normal case
    2) ... tail      ---> degenerate
    3) tail          ---> normal case
    4) ...           ---> degenerate
    """
    head = []
    tail = []

    current = head

    for item in liste:

        if item is ...:
            current = tail
            continue

        current.append(item)

    return (head, tail)


def prepare_params(params: Union[List[Any], List[Tuple[str, str]]]) \
        -> List[Any]:
    """
    Prepare a list of parameters for a command line invocation

    Must also ensure there are no whitespace separated entries.

    We use 'str' on all items because of potential special instances
    such as LazyEnvValue.
    """
    liste = flatten(params)
    new_liste = []

    for item in liste:
        if isinstance(item, tuple) or isinstance(item, Param):
            new_liste.append(str(item[0]))
            new_liste.append(str(item[1]))
            continue
        new_liste.append(str(item))

    return new_liste


class JsonObject(dict):
    """
    Utility class for handling JSON objects
    """

    @classmethod
    def from_string(cls, json_str: str):
        """
        Build an instance from a JSON string
        """
        json_obj = json.loads(json_str)
        return cls(json_obj)

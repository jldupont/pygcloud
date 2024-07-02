"""
@author: jldupont
"""
from typing import List, Any, Tuple


def flatten(*liste: List[Any] | Tuple[Any]):
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


def prepare_params(params: List[Any] | List[Tuple[str, str]]) -> List[Any]:
    """
    Prepare a list of parameters for a command line invocation
    """
    liste = flatten(params)
    new_liste = []

    for item in liste:
        if isinstance(item, tuple):
            new_item = f"{item[0]}={item[1]}"
            new_liste.append(new_item)
            continue
        new_liste.append(item)

    return new_liste

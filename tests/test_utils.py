"""@author: jldupont"""

import pytest
from pygcloud.utils import flatten, split_head_tail, prepare_params


@pytest.mark.parametrize("liste,expected", [
    ([1, 2, 3],    [1, 2, 3]),
    ([1, [2, 3]], [1, 2, 3]),
    ([1, (2, 3)],   [1, (2, 3)]),
    ([[(1, 2)]],   [(1, 2)])
])
def test_flatten(liste, expected):
    assert flatten(liste) == expected


@pytest.mark.parametrize(
    "liste,expected", [
        (("head", ..., "tail"),
            (["head"], ["tail"])),
        (("head",),
            (["head",], [])),
        ((...,),
            ([], [])),
        ((..., "tail"),
            ([], ["tail"])),
        ((),
            ([], []))
    ]
)
def test_split_head_tail_base(liste, expected):
    head, tail = split_head_tail(liste)
    assert head == expected[0]
    assert tail == expected[1]


@pytest.mark.parametrize("inp, expected", [
    (("key", "value"),
        ["key", "value"]),
    (["a", [("c", "d")]],
        ["a", "c", "d"])
])
def test_prepare_params(inp, expected):
    assert prepare_params(inp) == expected

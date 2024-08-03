"""
@author: jldupont
"""

import pytest
from pygcloud.gcp.labels import LabelGenerator


def test_labels(mock_sn, sn1, sn2):

    mock_sn.use(sn1)
    mock_sn.use(sn2)

    labels = mock_sn.compute_use_entries()

    assert labels == [
        ("pygcloud-use-0", "ns1--name1"),
        ("pygcloud-use-1", "ns2--name2"),
    ], print(labels)

    result = mock_sn.generate_use_labels()
    assert result == [
        "--labels",
        "pygcloud-use-0=ns1--name1,pygcloud-use-1=ns2--name2",
    ], print(result)


@pytest.mark.parametrize(
    "ns, name, expected",
    [
        ("ns", "name", "ns--name"),
        ("ns--", "name", ValueError),  # double dash
        ("ns", "name--", "ns--bmFtZS0t"),  # because it will get encoded
        ("ns", "a" * 63, ValueError),  # because it is too long
        ("ns", "?" * 48, ValueError),  # because too long (ns--...)
    ],
)
def test_label_generator(ns, name, expected, mock_sn_class):
    """
    NOTE Encoding generates longer sequences to the input
    """
    sn = mock_sn_class(name, ns)

    if isinstance(expected, str):
        result = LabelGenerator.generate_label(sn)
        assert result == expected, print(result)
    else:
        with pytest.raises(expected):
            LabelGenerator.generate_label(sn)

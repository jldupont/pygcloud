"""
@author: jldupont
"""


def test_labels(mock_sn, sn1, sn2):

    mock_sn.use(sn1)
    mock_sn.use(sn2)

    labels = mock_sn.compute_use_entries()

    assert labels == [
        ("pygcloud-use-0", "ns1--name1"),
        ("pygcloud-use-1", "ns2--name2")
    ], print(labels)

    result = mock_sn.generate_use_labels()
    assert result == [
        "--labels", "pygcloud-use-0=ns1--name1,pygcloud-use-1=ns2--name2"
    ], print(result)

"""
@author: jldupont
"""
import pytest
import re
from pygcloud.gcp.utils import Codec


REGEX = re.compile(r"^[a-zA-Z0-9\-\_]*$")


@pytest.mark.parametrize("input", [
    "_",
    "--",
    "abc",  # YWJj
    "bonjour",  # Ym9uam91cg==
    "allo",  # YWxsbw==
])
def test_codec(input):
    """
    Make sure to include test cases that generate
    '=' padding during encoding
    """
    encoded = Codec.encode(input)
    assert len(encoded) > len(input)

    #
    # Make sure we only have expected characters
    #
    assert REGEX.match(encoded) is not None

    result = Codec.decode(encoded)

    assert result == input, print(result)


def test_codec_invalid_decode():

    input = "invalid="

    with pytest.raises(ValueError):
        Codec.decode(input)

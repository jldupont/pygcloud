"""@author: jldupont"""
import os
from dataclasses import dataclass

from pygcloud.models import Param, EnvParam, Result


@dataclass
class X:
    NAME = "X"
    PARAM = "X"


@dataclass
class Y(X):
    NAME = "Y"


def test_param():
    p = Param("key", "value")
    assert p.key == "key"


def test_unpack_tuple():

    t = ("key", "value")
    key, value = t

    assert key == "key"
    assert value == "value"


def test_param_as_tuple():
    p = Param("key", "value")
    assert p[0] == "key"
    assert p[1] == "value"

    assert len(p) == 2

    key, value = p
    assert key == "key"
    assert value == "value"


def test_dataclass():
    y = Y()
    assert y.NAME == "Y"
    assert y.PARAM == "X"


def test_sys_env():

    first_key = list(os.environ.keys())[0]
    first_value = os.environ.get(first_key)

    p = EnvParam("--key", first_key)

    assert p[0] == "--key"
    assert p[1] == first_value


def test_result_repr():

    r = Result(success=True, message="msg", code=0)
    expected = """Result(success=True, message='msg', code=0)"""

    assert repr(r) == expected, \
        print(r)

    assert str(r) == expected, \
        print(str(r))

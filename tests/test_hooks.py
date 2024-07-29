"""
@author: jldupont
"""
from pygcloud.hooks import Hooks


def test_hooks_count():
    """
    There is a minimum defined and having
    access to those is a good test
    """
    points = Hooks.get_points()
    assert len(points) >= 4, print(points)


def test_hooks_callback():

    Hooks.clear_callbacks()

    called = False

    def callback():
        nonlocal called
        called = True

    Hooks.register_callback("test", callback)
    Hooks.execute("test")

    assert called

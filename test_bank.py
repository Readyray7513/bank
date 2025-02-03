import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello, world") == 0

def test_value_h():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("H") == 20

def test_value_other():
    assert value("goodbye") == 100
    assert value("123") == 100
    assert value("") == 100







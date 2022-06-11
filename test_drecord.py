# pylint: disable=missing-function-docstring,missing-module-docstring,no-member

from drecord import r


def test_r():
    assert r(a=1, b=2, c=3) == r(a=1, b=2, c=3)
    assert r(a=1, b=2, c=3) == (1, 2, 3)

    assert r(a=1, b=2, c=3).c == 3
    assert r(a=1, b=2, c=3)[-1] == 3

    assert len(r(a=1, b=2, c=3)) == 3

    record = r(a=0, b=1, c=2, d=3, e=4, f=5, g=5)

    assert r(**record.__dict__) == record


def test_r_slicing():

    record = r(a=0, b=1, c=2, d=3, e=4, f=5, g=5)
    similar = tuple(record)

    assert record[1:4] == similar[1:4]

    assert record["b":"e"] == similar[1:4]


def test_r_replace():

    record = r(a=0, b=1, c=2)
    assert record(b=3, c=4) == r(a=0, b=3, c=4)

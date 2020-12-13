import pytest

# To run ONLY this func: py.test -m first_mark

@pytest.mark.first_mark
def test_method1():
    x=3
    y=7
    assert x==y

# To run: py.test -m second_mark
# The result is: 1 passed, 2 deselected, 2 warnings in 0.01s
# Warnings can be disabled or markers registered in pytest.ini

@pytest.mark.second_mark
def test_method2():
    x=3
    y=7
    assert x+y==10


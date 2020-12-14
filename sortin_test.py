import pytest

arr1 = [["katia",23],["Andy",2],["Charlotte",12]]

def sorter(arr):
    return sorted(arr, key=lambda x: x[1])

@pytest.mark.sorter
def test_method1():
    assert sorter(arr1) == [['Andy', 2], ['Charlotte', 12], ['katia', 23]]
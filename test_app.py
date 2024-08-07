import pytest
from app import add
def test_add():
    assert add(2,3) == 5
    assert add(-1,4) == 3
    assert add(-2,-2) == -4
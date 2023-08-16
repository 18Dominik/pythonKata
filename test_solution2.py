import pytest
from solution2 import Dictionary
#run test with pytest test_solution.py

@pytest.fixture
def call_newentry():
    t=Dictionary()
    a= t.newentry("Cherry", "fruit")
    return t


def test_returned_dict(call_newentry):
    output = call_newentry
    assert isinstance(output.dic, dict)

def test_newentry(call_newentry):
    output = call_newentry
    assert list(output.dic.keys())[1] == "Cherry"
    assert list(output.dic.values())[1] == "fruit"










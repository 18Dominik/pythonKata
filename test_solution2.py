import pytest
from solution2 import Dictionary
#run test with pytest test_solution.py

@pytest.fixture
def call_newentry():
    d=Dictionary()
    #a= d.newentry("Apple", "fruit")
    return d


def test_returned_dict(call_newentry):
    output = call_newentry
    assert isinstance(output, Dictionary)








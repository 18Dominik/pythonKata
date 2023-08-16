import pytest
#run test with pytest test_solution.py

@pytest.fixture
def call_newentry():
    d=Dictionary()
    return d.newentry("Apple", "fruit")


def test_returned_dict(call_newentry):
    output = call_newentry
    assert isinstance(output, dict)







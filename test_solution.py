import pytest
from solution import count_ips


@pytest.fixture
def call_count_ips():
    return count_ips('logfile.txt')


def test_returned_dict(call_count_ips):
    output = call_count_ips
    assert isinstance(output, dict)


def test_basic_read(call_count_ips):
    output = call_count_ips
    assert len(output) == 22



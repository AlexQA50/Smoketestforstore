import pytest

"""Перед и в конце всех тестов"""


@pytest.fixture(scope="module")
def start_and_finish():
    print("  The test has started!!!!")
    yield
    print("  The test is over!!!")

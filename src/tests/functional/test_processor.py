import pytest
from src.data.processor import DataProcessor


@pytest.fixture
def data_processor():
    return DataProcessor()


def test_process_content(data_processor):
    content = "1-3, 5\n2, 4-6"
    expected_result = [1, 2, 2, 3, 4, 5, 5, 6]
    assert data_processor.process_content(content) == expected_result


def test_merge_sort(data_processor):
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected_result = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert data_processor._DataProcessor__merge_sort(unsorted_list) == expected_result  # noqa: E501


def test_merge(data_processor):
    left = [1, 3, 5]
    right = [2, 4, 6]  # noqa: E501
    expected_result = [1, 2, 3, 4, 5, 6]
    assert data_processor._DataProcessor__merge(left, right) == expected_result

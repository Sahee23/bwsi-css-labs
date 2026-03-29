import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_mixed_pos_and_neg():
    assert max_subarray_sum(nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
def test_all_neg():
    assert max_subarray_sum(nums = [-8, -3, -6, -2, -5, -4]) == -2
def test_all_pos():
    assert max_subarray_sum(nums = [2, 3, 1, 5]) == 11
def test_single_element():
    assert max_subarray_sum(nums = [-5]) == -5
def test_max_location():
    # max at beginning
    assert max_subarray_sum(nums = [10, -2, -3, -4]) == 10
    # max at end
    assert max_subarray_sum(nums = [-1, -2, 3, 5]) == 8
    # max at middle
    assert max_subarray_sum(nums = [-2, -3, 4, -1, -2, 1, 5, -3]) == 7
def test_alternating_pos_and_negs():
    assert max_subarray_sum(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5]) == 5
def test_empty_list():
    assert max_subarray_sum(nums=[]) == 0
if __name__ == "__main__":
    pytest.main()
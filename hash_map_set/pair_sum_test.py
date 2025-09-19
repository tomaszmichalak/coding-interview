import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def pair_sum_unsorted(numbers: list[int], expected: int) -> list[int]:
    num_map = {}
    # populate map
    for i, num in enumerate(numbers):
        num_map[num] = i
    log.debug(f"Numbers dict {num_map}")

    # check if complementary number exists
    for i, num in enumerate(numbers):
        search_item = expected - num
        if search_item in num_map:
            return sorted([i, num_map[search_item]])
    return []

def pair_sum_unsorted_one_phase(numbers: list[int], expected: int) -> list[int]:
    num_map = {}

    for i, num in enumerate(numbers):
        search_item = expected - num
        if search_item in num_map:
            return sorted([i, num_map[search_item]])
        else:
            num_map[num] = i
    return []


def test_pair_sum_unsorted():
    assert pair_sum_unsorted([], 10) == []
    assert pair_sum_unsorted([1], 10) == []
    assert pair_sum_unsorted([1, 2], 10) == []
    assert pair_sum_unsorted([1, 0, 9], 10) == [0, 2]
    assert pair_sum_unsorted([1, 1, 0, 9], 10) == [0, 3]

def test_pair_sum_unsorted_one_phase():
    assert pair_sum_unsorted_one_phase([], 10) == []
    assert pair_sum_unsorted_one_phase([1], 10) == []
    assert pair_sum_unsorted_one_phase([1, 2], 10) == []
    assert pair_sum_unsorted_one_phase([1, 0, 9], 10) == [0, 2]
    assert pair_sum_unsorted_one_phase([1, 1, 0, 9], 10) == [1, 3] # duplicate, but still good
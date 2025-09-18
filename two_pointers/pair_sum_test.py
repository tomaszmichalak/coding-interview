import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

def pair_sum_brute_force(numbers: list[int], expected: int) -> list[int]:
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            log.debug(f"Checking... [number[{i}]: {numbers[i]}, number[{j}]: {numbers[j]}]")
            if (numbers[i] + numbers[j] == expected):
                return [numbers[i], numbers[j]]
    return []

def pair_sum_sorted(numbers: list[int], expected: int) -> list[int]:
    if (len(numbers) < 2):
        return []
    numbers.sort()
    log.debug(f"Sorted... {numbers}")

    left = 0
    right = len(numbers) - 1
    while(left < right):
        sum: int = numbers[left] + numbers[right]
        if (sum == expected):
           return [numbers[left], numbers[right]]
        elif (sum < expected):
           left = left + 1
        else:
           right = right -1
    return []


def test_pair_sum_brute_force():
    assert pair_sum_brute_force([], 10) == []
    assert pair_sum_brute_force([1], 10) == []
    assert pair_sum_brute_force([1, 2], 10) == []
    assert pair_sum_brute_force([1, 0, 9], 10) == [1, 9]
    assert pair_sum_brute_force([1, 1, 0, 9], 10) == [1, 9]

def test_pair_sum_sorted():
    assert pair_sum_sorted([], 10) == []
    assert pair_sum_sorted([1], 10) == []
    assert pair_sum_sorted([1, 2], 10) == []
    assert pair_sum_sorted([1, 1, 9, 10], 10) == [1, 9]
    assert pair_sum_sorted([1, 1, 0, 9, 10], 10) == [0, 10]
    assert pair_sum_sorted([1, 2, 3, 4, 5, 8, 10], 10) == [2, 8]

def __main__():
    test_pair_sum_sorted()
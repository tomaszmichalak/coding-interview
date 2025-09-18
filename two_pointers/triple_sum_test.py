import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def triple_sum_brute_force(numbers: list[int], expected: int) -> list[list[int]]:
    results: list[list[int]] = []
    numbers_length: int = len(numbers)
    for i in range (numbers_length):
        for j in range (i + 1, numbers_length):
            for k in range(j + 1, numbers_length):
                if (numbers[i] + numbers[j] + numbers[k] == expected):
                    result: list[int] = [numbers[i], numbers[j], numbers[k]]
                    result.sort()
                    results.append(result)
    results.sort()
    return results

def triple_sum_brute_force_unique(numbers: list[int], expected: int) -> list[list[int]]:
    result_set: set = set()
    numbers_length: int = len(numbers)
    for i in range (numbers_length):
        for j in range (i + 1, numbers_length):
            for k in range(j + 1, numbers_length):
                if (numbers[i] + numbers[j] + numbers[k] == expected):
                    triple = tuple(sorted([numbers[i], numbers[j], numbers[k]]))
                    result_set.add(triple)
    return sorted([list(t) for t in result_set])

def triple_sum_sorted(numbers: list[int], expected: int) -> list[list[int]]:
    result_set: set = set()
    sorted_numbers = sorted(numbers)
    for i in range (0, len(sorted_numbers) - 2):
        log.debug(f"Checking sum for {sorted_numbers[i]}, from {sorted_numbers[i+1]} to {sorted_numbers[-1]}")
        left = i + 1;
        right = len(sorted_numbers) - 1
        while (left < right):
            expected_sum = expected - sorted_numbers[i]
            calculated_sum = sorted_numbers[left] + sorted_numbers[right]
            if  calculated_sum == expected_sum:
                result_set.add(tuple(sorted([sorted_numbers[i], sorted_numbers[left], sorted_numbers[right]])))
                break
            elif calculated_sum < expected_sum:
                left = left + 1
            else:
                right = right - 1
    log.debug(f"result_set: {result_set}")
    return sorted([list(t) for t in result_set])


def test_brute_force():
    assert triple_sum_brute_force([0, -1, 2, -3, 1], 0) == [[-3, 1, 2], [-1, 0, 1]]
    assert triple_sum_brute_force_unique([0, -1, 2, -3, 1, 1], 0) == [[-3, 1, 2], [-1, 0, 1]]
    assert triple_sum_sorted([-3, -1, 0, 1, 1, 2], 0) == [[-3, 1, 2], [-1, 0, 1]]

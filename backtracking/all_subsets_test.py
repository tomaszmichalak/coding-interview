import logging
import sys
from collections import Counter

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def find_all_subsets(numbers: list[int]) -> list[list[int]]:
    if not numbers:
        return [[]]
    elif len(numbers) == 1:
        return [[], numbers[:]]
    result = []
    backtrack(numbers, [], set(), result)
    return result

def backtrack(numbers: list[int],
        candidate: list[int],
        used: set[int],
        result: list[list[int]]):
    if candidate in result:
        return
    else:
        result.append(candidate[:])
    for num in numbers:
        if num not in used:
            candidate.append(num)
            used.add(num)
            backtrack(numbers, candidate, used, result)
            candidate.pop()
            used.remove(num)

def find_all_subsets_inc_exc(numbers: list[int]) -> list[list[int]]:
    result = []
    backtrack_inc_exc(numbers, [], 0, result)
    return result

def backtrack_inc_exc(numbers: list[int],
        candidate: list[int],
        index: int,
        result: list[list[int]]):
    log.debug(f"Numbers dict {candidate}")
    if index == len(numbers):
        result.append(candidate[:])
        return
    candidate.append(numbers[index])
    backtrack_inc_exc(numbers, candidate, index + 1, result)
    candidate.pop()
    backtrack_inc_exc(numbers, candidate, index + 1, result)
    

def test_find_all_subsets_with_duplicates():
    assert find_all_subsets([]) == [[]]
    assert find_all_subsets([1]) == [[], [1]]
    assert find_all_subsets([1, 2]) == [[], [1], [1, 2], [2], [2, 1]]
    assert find_all_subsets([1, 2, 3]) == [
        [],
        [1], [1,2], [1, 2, 3], [1,3], [1, 3, 2], 
        [2], [2,1], [2, 1, 3], [2,3], [2, 3, 1], 
        [3], [3,1], [3, 1, 2], [3,2], [3, 2, 1]
    ]

def test_find_all_subsets_inc_exc():
    assert find_all_subsets_inc_exc([]) == [[]]
    assert compare(find_all_subsets_inc_exc([1]), [[], [1]])
    assert compare(find_all_subsets_inc_exc([1, 2]), [[], [1], [1, 2], [2]])
    assert compare(find_all_subsets_inc_exc([4, 5, 6]), [
        [],
        [4], [4,5], [4, 5, 6], [4,6],
        [5], [5,6],
        [6]
    ])

def compare(result: list[list[int]], expected: list[list[int]]) -> bool:
    if len(result) != len(expected):
        return False
    return Counter(map(tuple, expected)) == Counter(map(tuple, result))
    
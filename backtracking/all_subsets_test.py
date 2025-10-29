import logging
import sys

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

def test_find_all_subsets():
    assert find_all_subsets([]) == [[]]
    assert find_all_subsets([1]) == [[], [1]]
    assert find_all_subsets([1, 2]) == [[], [1], [1, 2], [2], [2, 1]]
    assert find_all_subsets([1, 2, 3]) == [
        [],
        [1], [1,2], [1, 2, 3], [1,3], [1, 3, 2], 
        [2], [2,1], [2, 1, 3], [2,3], [2, 3, 1], 
        [3], [3,1], [3, 1, 2], [3,2], [3, 2, 1]
    ]

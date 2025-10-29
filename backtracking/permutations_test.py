import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def find_all_permutations(numbers: list[int]) -> list[list[int]]:
    if not numbers:
        return []
    elif len(numbers) == 1:
        return [numbers[:]]
    result = []
    backtrack_permutations(numbers, [], set(), result)
    return result

def backtrack_permutations(numbers: list[int],
                        candidate: list[int],
                        used: set[int],
                        result: list[list[int]]):
    if len(candidate) == len(numbers):
        result.append(candidate[:])
        return
    for num in numbers:
        if num not in used:
            candidate.append(num)
            used.add(num)
            backtrack_permutations(numbers, candidate, used, result)
            candidate.pop()
            used.remove(num)




def test_find_all_permutations():
    assert find_all_permutations([]) == []
    assert find_all_permutations([1]) == [[1]]
    assert find_all_permutations([1, 2]) == [[1, 2], [2, 1]]
    assert find_all_permutations([1, 2, 3]) == [
        [1, 2, 3], [1, 3, 2], 
        [2, 1, 3], [2, 3, 1], 
        [3, 1, 2], [3, 2, 1]
    ]

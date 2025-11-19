from inspect import stack
import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("pop from empty stack")
    def is_empty(self):
        return len(self.items) == 0

def next_largest_number(nums: list[int]) -> list[int]:
    candidates = Stack()
    if len(nums) == 0: return []
    if len(nums) == 1: return [-1]
    result = [-1] * len(nums)
    for idx in range(len(nums) - 1, -1, -1):
        num = nums[idx]
        log.debug(f"num: {num}, candidates: {candidates.items}, result: {result}")
        while not candidates.is_empty() and num >= candidates.peek():
            candidates.pop()
        if candidates.is_empty():
            candidates.push(num)
            continue
        result[idx] = candidates.peek()
        candidates.push(num)
    return result

def test_stack():
    assert next_largest_number([]) == []
    assert next_largest_number([1]) == [-1]
    assert next_largest_number([1, 2]) == [2, -1]
    assert next_largest_number([1, 2, 2]) == [2, -1, -1]
    assert next_largest_number([5, 2, 3, 6, 1]) == [6, 3, 6, -1, -1]
    assert next_largest_number([5, 6, 2, 3, 1]) == [6, -1, 3, -1, -1]
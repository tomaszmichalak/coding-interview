import logging
import sys
import math

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def is_happy_number(n: int) -> bool:
    if n == 1:
        return True
    slow = n
    fast = get_next_number(n)
    while slow != fast:
        slow = get_next_number(slow)
        fast = get_next_number(get_next_number(fast))
        if slow == 1:
            return True
    return False

def get_next_number(n: int) -> int:
    total_sum = 0
    while n != 0:
        res = n % 10
        total_sum += res ** 2
        n = math.floor(n / 10)
    return total_sum

def test_get_next_number():
    assert get_next_number(0) == 0
    assert get_next_number(1) == 1
    assert get_next_number(2) == 4
    assert get_next_number(10) == 1
    assert get_next_number(12) == 5
    assert get_next_number(123) == 14
    assert get_next_number(1234) == 30

def test_is_happy_number():
    assert is_happy_number(1) == True
    assert is_happy_number(7) == True # 7 -> 49 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 ...
    assert is_happy_number(10) == True # 10 -> 1
    assert is_happy_number(19) == True # 19 -> 82 -> 68 -> 100 -> 1
    assert is_happy_number(23) == True # 23 -> 13 -> 10 -> 1
    assert is_happy_number(2) == False # 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 ...
    assert is_happy_number(3) == False # 3 -> 9 -> 81 -> 65 -> 61 -> 37 ...
    assert is_happy_number(4) == False # 4 -> 16 -> 37 ...
    assert is_happy_number(37) == False # 37 -> 58 ...
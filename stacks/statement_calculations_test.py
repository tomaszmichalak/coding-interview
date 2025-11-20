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

def calculate(s: str) -> list[int]:
    stack = Stack()
    total = 0
    
    sign = 1
    number = 0
    local_total = 0
    for c in s:
        if c.isdigit():
            number = number * 10 + int(c)
        elif c == "-":
            local_total += number * sign
            number = 0
            sign = -1
        elif c == "+":
            local_total += number * sign
            number = 0
            sign = 1
        elif c == "(":
            stack.push(local_total)
            stack.push(sign)
            local_total = 0
            number = 0
            sign = 1
        elif c == ")":
            local_total += number * sign
            sign = stack.pop()
            previous_total = stack.pop()
            local_total = previous_total + local_total * sign
            number = 0
            sign = 1
        else:
            raise ValueError(f"Invalid character: {c}")
        log.debug(f"char: {c}, local_total: {local_total}, number: {number}, sign: {sign}, stack: {stack.items}")
    total += local_total + number * sign

    return total

def test_stack():
    assert calculate("1") == 1
    assert calculate("1+2") == 3
    assert calculate("2-1") == 1
    assert calculate("2-1-1") == 0
    assert calculate("2-(1-1)") == 2
    assert calculate("2-(1-1)+(2-1)") == 3
    assert calculate("2-(1-(1-2))") == 0
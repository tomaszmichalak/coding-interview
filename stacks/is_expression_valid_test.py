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
    def is_empty(self):
        return len(self.items) == 0

def is_expression_valid(s: str) -> bool:
    if len(s) == 0:
        return False
    stack = Stack()
    parentheses = {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in parentheses:
            stack.push(c)
        else:
            last_c = stack.pop()
            if c != parentheses[last_c]:
                return False
    if not stack.is_empty():
        return False
    return True

def test_stack():
    assert is_expression_valid("") == False
    assert is_expression_valid("(") == False
    assert is_expression_valid("()") == True
    assert is_expression_valid("([])") == True
    assert is_expression_valid("([)") == False
    assert is_expression_valid("([{") == False
    assert is_expression_valid("([{}]{})") == True
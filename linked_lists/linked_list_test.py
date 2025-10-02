import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

# singly linked list node
class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

# double linked list node
class DoubleListNode:
    def __init__(self, val: int, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

def print_linked_list(head: ListNode) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_print_linked_list():
    assert print_linked_list(head) == [1, 2, 3, 4, 5]
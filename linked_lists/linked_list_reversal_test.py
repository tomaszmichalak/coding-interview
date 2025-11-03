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

def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def reverse_linked_list_recursive(head: ListNode) -> ListNode:
    if head.next:
        new_head = reverse_linked_list_recursive(head.next)
        prev = head.next
        prev.next = head
        head.next = None
        return new_head
    else:
        return head

def print_linked_list(head: ListNode) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_reverse_linked_list():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head = reverse_linked_list(head)
    assert print_linked_list(reversed_head) == [5, 4, 3, 2, 1]

def test_reverse_linked_list_recursive():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head = reverse_linked_list_recursive(head)
    assert print_linked_list(reversed_head) == [5, 4, 3, 2, 1]
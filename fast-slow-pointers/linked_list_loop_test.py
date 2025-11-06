import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def contains_loop_naive(head: ListNode) -> bool:
    if not head.next:
        return False
    visited = {}
    node = head
    while node:
        if node.val in visited:
            return True
        visited[node.val] = node
        node = node.next
    return False

# Floyd's Cycle Detection
def contains_loop_floyd(head: ListNode) -> bool:
    if not head.next:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def test_contains_loop_single_item():
    assert contains_loop_naive(ListNode(0)) == False

# 0 -> 1
def test_contains_loop_two_items_no_cycle():
    node_0 = ListNode(0)
    node_1 = ListNode(1)
    node_0.next = node_1
    assert contains_loop_naive(node_0) == False
    assert contains_loop_floyd(node_0) == False

# 0 <-> 1
def test_contains_loop_two_items_cycle():
    node_0 = ListNode(0)
    node_1 = ListNode(1)
    node_0.next = node_1
    node_1.next = node_0
    assert contains_loop_naive(node_0) == True
    assert contains_loop_floyd(node_0) == True

# 0 -> 1 -> 2
def test_contains_loop_three_items_no_cycle():
    node_0 = ListNode(0)
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_0.next = node_1
    node_1.next = node_2
    assert contains_loop_naive(node_0) == False
    assert contains_loop_floyd(node_0) == False

# 0 -> 1 <-> 2
def test_contains_loop_short_cycle():
    node_0 = ListNode(0)
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_0.next = node_1
    node_1.next = node_2
    node_2.next = node_1
    assert contains_loop_naive(node_0) == True
    assert contains_loop_floyd(node_0) == True

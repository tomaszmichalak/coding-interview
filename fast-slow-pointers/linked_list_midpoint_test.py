import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def find_middle(head: ListNode) -> int:
    if not head.next:
        return head.val
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val


def test_find_middle_single_item():
    assert find_middle(ListNode(0)) == 0

# 0 -> 1
def test_find_middle_two_items():
    node_0 = ListNode(0)
    node_1 = ListNode(1)
    node_0.next = node_1
    assert find_middle(node_0) == 1

# 0 -> 1 -> 2
def test_find_middle_three_items():
    node_0 = ListNode(0)
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_0.next = node_1
    node_1.next = node_2
    assert find_middle(node_0) == 1

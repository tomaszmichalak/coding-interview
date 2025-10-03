import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

def remove_kth_last_node_brute(head: ListNode, k: int) -> ListNode:
    if k == 0:
        return head
    
    # to remove first node
    dummy = ListNode(-1)
    dummy.next = head
    
    curr = dummy
    while curr:
        len = list_lenght(curr)
        if len == k + 1:
            curr.next = curr.next.next
            return dummy.next
        curr = curr.next
    return head


def remove_kth_last_node_leader(head: ListNode, k: int) -> ListNode:
    if k == 0:
        return head    
    # to remove first node
    dummy = ListNode(-1)
    dummy.next = head
    
    trailer = dummy
    leader = dummy
    while trailer:
        while k > 0:
            if not leader.next:
                return dummy.next
            leader = leader.next
            k -= 1
        if not leader.next:
            trailer.next = trailer.next.next
            return dummy.next
        trailer = trailer.next
        leader = leader.next
    return head

def list_lenght(head: ListNode) -> int:
    len = 0
    while head:
        head = head.next
        len += 1
    return len

def print_linked_list(head: ListNode) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_remove_kth_last_node_brute():
    head = ListNode(1)
    assert print_linked_list(remove_kth_last_node_brute(head, 0)) == [1]
    head = ListNode(1, ListNode(2))
    assert print_linked_list(remove_kth_last_node_brute(head, 1)) == [1]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert print_linked_list(remove_kth_last_node_brute(head, 2)) == [1, 2, 3, 5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert print_linked_list(remove_kth_last_node_brute(head, 5)) == [2, 3, 4, 5]

def test_remove_kth_last_node_leader():
    head = ListNode(1)
    assert print_linked_list(remove_kth_last_node_leader(head, 0)) == [1]
    head = ListNode(1, ListNode(2))
    assert print_linked_list(remove_kth_last_node_leader(head, 1)) == [1]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert print_linked_list(remove_kth_last_node_leader(head, 2)) == [1, 2, 3, 5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert print_linked_list(remove_kth_last_node_leader(head, 5)) == [2, 3, 4, 5]

import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def find_first_intersection_node(head_A: ListNode, head_B: ListNode) -> ListNode:
    ptr_A = head_A
    ptr_B = head_B

    ptr_A_switched = False
    ptr_B_switched = False
    while ptr_A and ptr_B and ptr_A.val != ptr_B.val:
        log.debug(f"ptr_A: {ptr_A.val if ptr_A else None}, ptr_B: {ptr_B.val if ptr_B else None}")
        # advance pointers A or switch to the head of the other list
        ptr_A = ptr_A.next
        if not ptr_A and not ptr_A_switched:
            ptr_A = head_B
            ptr_A_switched = True
        # advance pointer B or switch to the head of the other list
        ptr_B = ptr_B.next
        if not ptr_B and not ptr_B_switched:
            ptr_B = head_A
            ptr_B_switched = True
    return ptr_A


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

def test_linked_list_intersection():
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    head2 = ListNode(2, ListNode(3, ListNode(4)))
    assert print_linked_list(find_first_intersection_node(head1, head2)) == [2, 3, 4]

    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    head2 = ListNode(4)
    assert print_linked_list(find_first_intersection_node(head1, head2)) == [4]

    head1 = ListNode(1)
    head2 = ListNode(4)
    assert print_linked_list(find_first_intersection_node(head1, head2)) == []

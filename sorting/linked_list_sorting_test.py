import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

# quick sort requires random access through indexing, so it is not suitable for linked lists
# merge sort is more suitable for linked lists (O(n log n)) and can be done in place (O(1) space complexity)

# merge sort = divide and conquer
class ListNode:
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next

head = ListNode(3, 
                ListNode(2, 
                        ListNode(4, 
                                ListNode(5, 
                                        ListNode(1)))))
converted = [3, 2, 4, 5, 1]

def convert(head: ListNode) -> list[int]:
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

def test_convert():
    assert convert(head) == converted

def merge_sort(head: ListNode):
    if not head or not head.next:
        return head
    
    second_half_head = split(head)

    first_sorted_half = merge_sort(head)
    second_sorted_half = merge_sort(second_half_head)

    return merge(first_sorted_half, second_sorted_half)

def split(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second_half = slow.next
    slow.next = None
    return second_half

def merge(first_half: ListNode, second_half: ListNode) -> ListNode:
    dummy = ListNode(0)
    tail = dummy
    while first_half and second_half:
        if first_half.value <= second_half.value:
            tail.next = first_half
            first_half = first_half.next
        else:
            tail.next = second_half
            second_half = second_half.next
        tail = tail.next
    
    tail.next = first_half or second_half
    
    return dummy.next

def test_merge_sort():
    sorted_head = merge_sort(head)
    assert convert(sorted_head) == [1, 2, 3, 4, 5]
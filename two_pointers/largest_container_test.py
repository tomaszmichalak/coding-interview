import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def largest_container_brute_force(heights: list[int]):
    largest_container: int = 0
    for i in range (0, len(heights)):
        for j in range (i + 1, len(heights)):
            current_container = min(heights[i], heights[j]) * (j - 1)
            if (current_container > largest_container):
                largest_container = current_container
    return largest_container

def largest_container(heights: list[int]):
    largest_container: int = 0
    left = 0
    right = len(heights) - 1
    while (left < right):
        current_container = min(heights[left], heights[right]) * (right - left)
        if (current_container > largest_container):
            largest_container = current_container
        if (heights[left] < heights[right]):
            left += 1
        elif (heights[left] > heights[right]):
            right -= 1
        else:
            left += 1
            right -= 1
    return largest_container


def test_largest_container_brute_force():
    assert largest_container_brute_force([2, 7, 8, 3, 7, 6]) == 24

def test_largest_container():
    assert largest_container([2, 7, 8, 3, 7, 6]) == 24
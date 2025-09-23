import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

input_array = [3, 2, 4, 5, 1, 11, 6, 8, 7, 10, 9]
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            prev = j
            next = j + 1
            if arr[prev] > arr[next]:
                swap = arr[next]
                arr[next] = arr[prev]
                arr[prev] = swap
    return arr


def quick_sort(arr: list[int]) -> list[int]:
    quick_sort_partition(arr, 0, len(arr) - 1)
    return arr

def quick_sort_partition(arr: list[int], left: int, right: int):
    if left >= right:
        return
    pivot_index = partition(arr, left, right)
    quick_sort_partition(arr, left, pivot_index - 1)
    quick_sort_partition(arr, pivot_index, right)

def partition(arr: list[int], left: int, right: int) -> int:
    lo = left
    pivot = arr[right]
    for i in range(left, right):
        if arr[i] < pivot:
            swap(arr, lo, i)
            lo += 1
    swap(arr, lo, right)
    return lo

def swap(arr: list[int], left: int, right: int):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp


def test_bubble_sort():
    assert bubble_sort(input_array.copy()) == sorted_array

def test_quick_sort():
    inplace_sort_array = input_array.copy()
    assert quick_sort(inplace_sort_array) == sorted_array
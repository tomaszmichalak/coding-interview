import logging
import sys
from operator import itemgetter

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __eq__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented

        return self.start == other.start and self.end == other.end

# time complexity O(log(n))
def toIntervals(intervals: list[list[int]]) -> list[Interval]:
    result = []
    for i in range(len(intervals)):
        result.append(Interval(intervals[i][0], intervals[i][1]))
    return result

def fromIntervals(intervals: list[Interval]) -> list[list[int]]:
    result = []
    for i in range(len(intervals)):
        result.append([intervals[i].start, intervals[i].end])
    return result

# l1, l2 - sorted not overlaping list
def identify_intersections(l1: list[list[int]], l2: list[list[int]]) -> list[Interval]:
    intersections = []
    sorted_l1 = toIntervals(l1)
    sorted_l2 = toIntervals(l2)
    i, j = 0, 0
    while i < len(sorted_l1) and j < len(sorted_l2):
        A, B = sorted_l1[i], sorted_l2[j]
        if sorted_l1[i].start > sorted_l2[j].start:
            A, B = sorted_l2[j], sorted_l1[i]
        if A.end >= B.start:
            intersections.append(Interval(B.start, min(A.end, B.end)))
        if sorted_l1[i].end < sorted_l2[j].end:
            i += 1
        else:
            j += 1
    return intersections

def test_merge_overlaping():
    assert fromIntervals(identify_intersections([[1, 5]],[])) == []
    assert fromIntervals(identify_intersections([[1, 5]],[[6, 7]])) == []
    assert fromIntervals(identify_intersections([[1, 5]],[[4, 6]])) == [[4, 5]]
    assert fromIntervals(identify_intersections([[1, 5]],[[2, 3]])) == [[2, 3]]
    assert fromIntervals(identify_intersections([[1, 5], [7, 10]],[[2, 3], [4, 8]])) == [[2, 3], [4, 5], [7, 8]]

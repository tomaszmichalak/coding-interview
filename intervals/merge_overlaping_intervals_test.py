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

intervals = [[3,4], [7,8], [2,5], [6,7], [1,4]]
expected = [[1,5], [6,8]]

# time complexity O(log(n))
def sort(intervals: list[list[int]]) -> list[Interval]:
    sorted_intervals = sorted(intervals, key=itemgetter(0))
    result = []
    for i in range(len(sorted_intervals)):
        result.append(Interval(sorted_intervals[i][0], sorted_intervals[i][1]))
    return result

# time complexity O(n log(n)) - sorting + O(n) - merging
def merge_overlaping(intervals: list[list[int]]) -> list[Interval]:
    sorted_intervals = sort(intervals)
    merged = [sorted_intervals[0]]
    # time complexity O(n)
    for i in range(1, len(sorted_intervals)):
        last_interval = merged[-1]
        if last_interval.end >= sorted_intervals[i].start:
            merged[-1] = Interval(last_interval.start, max(sorted_intervals[i].end, last_interval.end))
        else:
            merged.append(sorted_intervals[i])
    return merged

def test_merge_overlaping():
    assert merge_overlaping(intervals) == sort(expected)
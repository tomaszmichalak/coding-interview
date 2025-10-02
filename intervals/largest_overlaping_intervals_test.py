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

def sort(intervals: list[list[int]]) -> list[Interval]:
    sorted_intervals = sorted(intervals, key=itemgetter(0))
    result = []
    for i in range(len(sorted_intervals)):
        result.append(Interval(sorted_intervals[i][0], sorted_intervals[i][1]))
    return result

# both start and end are inclusive
def largest_intersections_count(list: list[list[int]]) -> int:
    log.debug(f"input: {list}")
    count_by_index = {}
    largest_count = 1
    for i in range (len(list)):
        start = list[i][0]
        end = list[i][1]
        for j in range (start, end + 1):
            if j in count_by_index:
                count_by_index[j] += 1
                if count_by_index[j] > largest_count:
                    largest_count = count_by_index[j]
            else:
                count_by_index[j] = 1
    log.debug(f"count_by_index: {count_by_index}")
    return largest_count

# both start and end are inclusive
def largest_intersections_count_optimised(list: list[list[int]]) -> int:
    points = []
    for interval in list:
        points.append((interval[0], 'S1')) # S1 - priority over S2 (inclusive)
        points.append((interval[1], 'S2'))
    points.sort(key=lambda x: (x[0], x[1]))
    log.debug(f"points: {points}")

    current_count = 0
    largest_count = 1   
    for point in points:
        if point[1] == 'S1':
            current_count += 1
            if current_count > largest_count:
                largest_count = current_count
        else:
            if current_count > largest_count:
                largest_count = current_count
            current_count -= 1
    return largest_count

def test_merge_overlaping():
    assert largest_intersections_count([[1, 5]]) == 1
    assert largest_intersections_count([[1, 5], [6, 7]]) == 1
    assert largest_intersections_count([[1, 5], [2, 3]]) == 2
    assert largest_intersections_count([[1, 5], [2, 4], [2, 3]]) == 3
    assert largest_intersections_count([[1, 5], [2, 4], [4, 5]]) == 3

    assert largest_intersections_count_optimised([[1, 5]]) == 1
    assert largest_intersections_count_optimised([[1, 5], [6, 7]]) == 1
    assert largest_intersections_count_optimised([[1, 5], [2, 3]]) == 2
    assert largest_intersections_count_optimised([[1, 5], [2, 4], [2, 3]]) == 3
    assert largest_intersections_count_optimised([[1, 5], [2, 4], [4, 5]]) == 3
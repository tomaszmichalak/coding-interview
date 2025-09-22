import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

valid_data: list[list[int]] = [
    [1, 2, 3, 4, 5],
    [6, 0, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 0]
]

expected_data: list[list[int]] = [
    [1, 0, 3, 4, 0],
    [0, 0, 0, 0, 0],
    [11, 0, 13, 14, 0],
    [0, 0, 0, 0, 0]
]

def zero_striping_brute_force(matrix: list[list[int]]) -> list[list[int]]:
    zero_cells: set = set()
    log.debug(f"{type(zero_cells)}")
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                zero_cells.add(tuple([row, col]))
    for i in zero_cells:
        row, col = i[0], i[1]
        for i in range(len(matrix[row])):
            matrix[row][i] = 0
        for i in range(len(matrix)):
            matrix[i][col] = 0
    return matrix

def test_zero_striping_brute_force() -> None:
    assert zero_striping_brute_force(valid_data) == expected_data
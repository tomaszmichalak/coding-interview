import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

invalid_row_data = [
    [3, 0, 6, 0, 5, 0, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [1, 0, 2, 5, 0, 0, 3, 2, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [0, 3, 0, 0, 0, 8, 2, 5, 0],
    [0, 1, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 0, 0, 0]
]
invalid_column_data = [
    [3, 0, 6, 0, 5, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [1, 0, 0, 5, 0, 0, 3, 2, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [0, 3, 0, 0, 0, 8, 2, 5, 0],
    [0, 1, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 0, 0, 0]
]
invalid_subgrid_data = [
    [3, 7, 6, 0, 5, 0, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [1, 0, 0, 5, 0, 0, 3, 2, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [0, 3, 0, 0, 0, 8, 2, 5, 0],
    [0, 1, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 0, 0, 0]
]
valid_data = [
    [3, 0, 6, 0, 5, 0, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [1, 0, 0, 5, 0, 0, 3, 2, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [0, 3, 0, 0, 0, 8, 2, 5, 0],
    [0, 1, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 0, 0, 0]
]

def sudoku_is_valid(board: list[list[int]]) -> bool:
    # row_sets: list[set[int]] = [set() for _ in range(9)]
    row_sets: list[set[int]] = []
    column_sets: list[set[int]] = []
    for i in range(9):
        row_sets.append(set())
        column_sets.append(set())
    subgrid_sets: list[list[set[int]]] = [[set(), set(), set()],[set(), set(), set()],[set(), set(), set()]]

    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell == 0:
                continue
            if cell in row_sets[i]:
                log.debug(f"invalid row [{i}, {j}]={cell} for [{row_sets[i]}]")
                return False
            else:
                row_sets[i].add(cell)
            if cell in column_sets[j]:
                log.debug(f"invalid column [{i}, {j}]={cell} for [{column_sets[i]}]")
                return False
            else:
                column_sets[j].add(cell)
            subgrid_set = subgrid_sets[i // 3][j // 3]
            if cell in subgrid_set:
                log.debug(f"invalid subgrid [{i}, {j}]={cell} for [{subgrid_set}]")
                return False
            else:
                subgrid_sets[i // 3][j // 3].add(cell)

    log.debug(f"row_sets: {row_sets}")
    log.debug(f"column_sets: {column_sets}")
    return True



def test_sudoku_is_valid():
    assert sudoku_is_valid(invalid_row_data) == False
    assert sudoku_is_valid(invalid_column_data) == False
    assert sudoku_is_valid(invalid_subgrid_data) == False
    assert sudoku_is_valid(valid_data) == True


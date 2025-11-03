import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

res = 0

# n is the number of rows & columns
def safe_n_queens(n: int) -> int:
    dfs(0, set(), set(), set(), n)
    return res

def dfs(row: int, cols_set: set[int], diagonals_set: set[int], anti_diagonals_set: set[int], n: int) -> None:
    global res
    if (row == n):
        log.debug(f"Cols {cols_set}")
        res += 1
        return
    for col in range(n):
        curr_diagonal = row - col
        curr_anti_diagonal = row + col
        if col in cols_set or curr_diagonal in diagonals_set or curr_anti_diagonal in anti_diagonals_set:
            continue
        cols_set.add(col)
        diagonals_set.add(curr_diagonal)
        anti_diagonals_set.add(curr_anti_diagonal)
        dfs(row + 1, cols_set, diagonals_set, anti_diagonals_set, n)
        cols_set.remove(col)
        diagonals_set.remove(curr_diagonal)
        anti_diagonals_set.remove(curr_anti_diagonal)

def test_safe_n_queens():
    global res
    res = 0
    assert safe_n_queens(1) == 1
    res = 0
    assert safe_n_queens(2) == 0
    res = 0
    assert safe_n_queens(4) == 2

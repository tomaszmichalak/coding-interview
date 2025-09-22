import logging
import sys
from collections import deque


log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class TreeNode:
    def __init__(self, val: str):
        self.val = val
        self.left = None
        self.right = None
    def process(self, order: str) -> str:
        log.info(f"Calling val: {self.val}")
        return order + str(self.val)

root = TreeNode("4")
root_left = TreeNode("2")
root_right = TreeNode("5")
root_left_left = TreeNode("1")
root_right_left = TreeNode("6")
root_right_right = TreeNode("7")

root.left = root_left
root.right = root_right
root_left.left = root_left_left
root_right.left = root_right_left
root_right.right = root_right_right

def dfs_postorder(node: TreeNode, order: str) -> str:
    if node == None:
        return 0
    if node.left:
        order = dfs_postorder(node.left, order)
    if node.right:
        order = dfs_postorder(node.right, order)
    return node.process(order)

# finding the shortest path
def bfs(node: TreeNode, order: str) -> str:
    queue = deque([root])
    while queue: # implicitly convert d to a bool, which yields True if the deque contains any items and False if it is empty
        node = queue.popleft()
        order = node.process(order)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def test_dfs_postorder():
    assert dfs_postorder(root, "") == "126754"

def test_bfs():
    assert bfs(root, "") == "425167"
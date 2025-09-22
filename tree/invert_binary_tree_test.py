import logging
import sys
from collections import deque


log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(5, 
                TreeNode(1, 
                        TreeNode(7), 
                        TreeNode(6)
                ), 
                TreeNode(8, 
                        None, 
                        TreeNode(4))
                )
expectedRoot = TreeNode(5, 
                TreeNode(8, 
                        TreeNode(4),
                        None), 
                TreeNode(1, 
                        TreeNode(6),
                        TreeNode(7)))

def tree_dfs(node: TreeNode) -> list[int]:
    if node == None:
        return []
    result = [node.value]
    if node.left:
        result.append(tree_dfs(node.left))
    elif node.left or node.right:
        result.append([])
    if node.right:
        result.append(tree_dfs(node.right))
    elif node.left or node.right:
        result.append([])
    return result

def invert_tree_dfs(node: TreeNode) -> TreeNode:
    if node == None:
        return None
    if node.left:
        invert_tree_dfs(node.left)
    if node.right:
        invert_tree_dfs(node.right)
    tmp = node.left
    node.left = node.right
    node.right = tmp
    return node


def test_invert_tree_dfs():
    assert tree_dfs(root) == [5, [1, [7], [6]], [8, [], [4]]]
    assert tree_dfs(expectedRoot) == [5, [8, [4], []], [1, [6], [7]]]
    assert tree_dfs(invert_tree_dfs(root)) == tree_dfs(expectedRoot)
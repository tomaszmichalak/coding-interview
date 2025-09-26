import logging
import sys
from collections import deque


log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

inbalanced_root =  TreeNode(5,
            TreeNode(2,
                TreeNode(1),
                TreeNode(4,
                    TreeNode(3)
                )
            ),
            TreeNode(7,
                None,
                TreeNode(9,
                    TreeNode(6)
                )
            )
        )

balanced_root =  TreeNode(5,
            TreeNode(2,
                TreeNode(1),
                TreeNode(4,
                    TreeNode(3)
                )
            ),
            TreeNode(7,
                TreeNode(6),
                TreeNode(9,
                    TreeNode(8)
                )
            )
        )

def is_balanced_dfs(root: TreeNode) -> bool:
    height = checkSubtreeHeight(root)
    if height == -1:
        return False
    else:
        return True

def checkSubtreeHeight(node: TreeNode) -> int:
    left_height = 0
    right_height = 0
    if node.left:
        left_height = checkSubtreeHeight(node.left)
    if node.right:
        right_height = checkSubtreeHeight(node.right)
    if left_height == -1 or right_height == -1:
        return -1
    if abs(right_height - left_height) > 1:
        log.debug(f"detected inbalaced subtrees in node {node.val}")
        return -1
    else:
        return 1 + max(left_height, right_height)
    
def test_is_balanced_dfs():
    assert is_balanced_dfs(inbalanced_root) == False
    assert is_balanced_dfs(balanced_root) == True
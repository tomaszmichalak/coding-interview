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

with_11 =  TreeNode(1,
            TreeNode(2,
                TreeNode(4,
                    TreeNode(8),
                    TreeNode(9)
                ),
                TreeNode(5,
                    None,
                    TreeNode(11)
                )
            ),
            TreeNode(3,
                TreeNode(6),
                TreeNode(7)
            )
        )

no_11 =  TreeNode(1,
            TreeNode(2,
                TreeNode(4,
                    TreeNode(8),
                    TreeNode(9)
                ),
                TreeNode(5)
            ),
            TreeNode(3,
                TreeNode(6),
                TreeNode(7)
            )
        )


def get_rightmost_nodes(root: TreeNode) -> list[int]:
    right_nodes = []
    queue = deque([root])
    while queue:
        level_lenght = len(queue)
        for i in range (level_lenght):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            if i == level_lenght - 1: right_nodes.append(node.val)
    return right_nodes
    
def test_get_rightmost_nodes():
    assert get_rightmost_nodes(with_11) == [1, 3, 7, 11]
    assert get_rightmost_nodes(no_11) == [1, 3, 7, 9]

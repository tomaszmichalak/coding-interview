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

root =  TreeNode(1,
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
                TreeNode(7,
                    None,
                    TreeNode(14)
                )
            )
        )

root_smaller =  TreeNode(1,
            TreeNode(2,
                TreeNode(4,
                    TreeNode(8),
                    TreeNode(9)
                ),
                TreeNode(5,
                    TreeNode(11)
                )
            ),
            TreeNode(3,
                TreeNode(6),
                TreeNode(7)
            )
        )

# level 0: 0
# level 1: 1,              2
# level 2: 3,      4,      5,      6
# level 3: 7,8,    9,10,   11,12,  13,14
# left = 2 * parent.val + 1, right = 2 * parent.val + 2

def calc_widest_binary_tree_level(root: TreeNode) -> int:
    max_width = 0
    queue = deque([(root, 0)])
    while (queue):
        level_lenght = len(queue)
        for i in range(level_lenght):
            node_with_index = queue.popleft()
            node = node_with_index[0]
            index = node_with_index[1]
            log.debug(f"node: [{node.val}]")
            if i == 0:
                left_most_index = index
            if i == level_lenght - 1:
                right_most_index = index
            if node.left: queue.append((node.left, 2 * index + 1))
            if node.right: queue.append((node.right, 2 * index + 2))
            max_width = max(max_width, right_most_index - left_most_index + 1)
    return max_width

    
def test_get_rightmost_nodes():
    assert calc_widest_binary_tree_level(root) == 8
    assert calc_widest_binary_tree_level(root_smaller) == 4
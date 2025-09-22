import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

adjacency_map = { 
    0 : [1, 2, 3],
    1: [0],
    2: [0, 3, 4],
    3: [0, 2],
    4: [2]
}

adjacency_nodes = {}
for key in adjacency_map:
    adjacency_nodes.update({ key : GraphNode(key)})
for key, neighbors in adjacency_map.items():
    for neighbor in neighbors:
        adjacency_nodes[key].neighbors.append(adjacency_nodes[neighbor])

def deep_copy_dfs(node: GraphNode, cloned: dict[int, GraphNode], order: list[int]) -> GraphNode:
    cloned[node.val] = GraphNode(node.val)
    order.append(node.val)
    for neighbor in node.neighbors:
        if (neighbor.val in cloned):
            cloned[node.val].neighbors.append(cloned[neighbor.val])
        else:
            cloned[node.val].neighbors.append(deep_copy_dfs(neighbor, cloned, order))
    return cloned[node.val]

def test_deep_copy_dfs():
    order = []
    cloned = {}
    new_node = deep_copy_dfs(adjacency_nodes[0], cloned, order)
    log.debug(f"Cloned: {cloned.keys()}")
    log.debug(f"Order: {order}")
    assert len(cloned) == 5
    assert new_node.val == 0
    assert len(new_node.neighbors) == 3
    assert new_node.neighbors[0].val == 1
    assert new_node.neighbors[1].val == 2
    assert new_node.neighbors[2].val == 3
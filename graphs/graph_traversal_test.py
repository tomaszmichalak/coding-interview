import logging
import sys
from collections import deque

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
    def process(self):
        log.debug(f"Processing {self.val}...")

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

def dfs(node: GraphNode, visited: set[GraphNode], order: list[int]):
    visited.add(node)
    node.process()
    order.append(node.val)
    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, visited, order)

def bfs(node: GraphNode, visited: set[GraphNode], order: list[int]):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            node.process()
            order.append(node.val)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

def test_mapping():
    log.debug(f"adjacency_nodes: {adjacency_nodes}")
    assert len(adjacency_nodes[0].neighbors) == 3
    assert len(adjacency_nodes[1].neighbors) == 1
    assert len(adjacency_nodes[2].neighbors) == 3
    assert len(adjacency_nodes[3].neighbors) == 2
    assert len(adjacency_nodes[4].neighbors) == 1

def test_dfs():
    order = []
    dfs(adjacency_nodes[0], set(), order)
    assert order == [0, 1, 2, 3, 4]

def test_bfs():
    order = []
    bfs(adjacency_nodes[0], set(), order)
    assert order == [0, 1, 2, 3, 4]
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
def cloneNode(node, nodes):
    if not node.val in nodes:
        nodes[node.val] = Node(node.val)
    neighbors = []
    for neighbor in node.neighbors:
        if not neighbor.val in nodes:
            cloneNode(neighbor, nodes)
        neighbors.append(nodes[neighbor.val])
    nodes[node.val].neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if not node:
            return None

        nodes = {}
        cloneNode(node, nodes)
        return nodes[1]
        



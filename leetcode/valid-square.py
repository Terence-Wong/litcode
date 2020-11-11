import math
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        edges = {}
        side = None
        arr = [p1, p2, p3, p4]
        for i, point in enumerate(arr):
            for x in range(i+1, 4):
                d = math.sqrt((point[0]-arr[x][0])**2 + (point[1]-arr[x][1])**2)
                if d in edges:
                    edges[d] += 1
                else:
                    edges[d] = 1
                
        edge_list = list(edges.values())
        return len(edges) == 2 and (edge_list[0]*2 == edge_list[1] or edge_list[0] == edge_list[1]*2)
        

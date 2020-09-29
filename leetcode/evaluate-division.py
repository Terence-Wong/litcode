from collections import defaultdict
class Solution(object):
    def dfs(self, visited, factor, target, node):
        if node == target:
            return factor

        if node in visited:
            return -1.0

        visited.append(node)
        for key, val in self.relation[node].items():
            temp = self.dfs(visited, factor*val, target, key)
            if not temp == -1.0:
                return temp

        return -1.0


    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.relation = defaultdict(dict)
        for eqn, val in zip(equations, values):
            a = eqn[0]
            b = eqn[1]
            X = float(val)
            self.relation[a][b] = X # a = X * b
            self.relation[b][a] = 1.0/val

        ans = []
        for q in queries:
            if q[1] in self.relation and q[0] in self.relation:
                ans.append(self.dfs([], 1, q[1], q[0]))
            else:
                ans.append(-1.0)

        return ans

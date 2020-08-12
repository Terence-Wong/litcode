class Solution(object):

    def nCr(self, n, r):
        return self.factorial(n) / self.factorial(r) / self.factorial(n-r)
    
    def factorial(self, n):
        if self.facts[n] == 0:
            ans = n * self.factorial(n-1)
            self.facts[n] = ans
            return ans
        
        return self.facts[n]


    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        
        self.facts = [0]*(rowIndex+1)
        self.facts[0] = 1
        self.facts[1] = 1
        ans = [0] * (rowIndex+1)
        for i, spot in enumerate(ans):
            ans[i] = self.nCr(rowIndex, i)

        return ans

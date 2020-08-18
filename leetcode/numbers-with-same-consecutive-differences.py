class Solution(object):
    def generate(self, ans, index, number):
        # base case
        if index == self.n:
            ans.append(int(number))
        # recursive case
        elif index == 0:
            for i in range(1,10):
                self.generate(ans, 1, str(i))            

        else:
            value = int(number[index-1]) + self.k 
            if value < 10:
                self.generate(ans, index+1, number+str(value))
            
            value = int(number[index-1]) - self.k
            if value > -1:
                self.generate(ans, index+1, number+str(value))

    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 0:
            return []
        elif N == 1:
            return [0,1,2,3,4,5,6,7,8,9]

        ans = []

        if K == 0:
            for i in range(1, 10):
                ans.append(int(str(i)*N))

            return ans

        self.n = N
        self.k = K
        self.generate(ans, 0, "")
        return ans

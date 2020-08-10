class Solution(object):
    def countAndSay(self, n):
        ans = 1
        for _ in range(0, n-1):
            ans = self.do(ans)

        return str(ans)

    def do(self, n):
        """
        :type n: int
        :rtype: str
        """

        prev = -1
        total = 0
        ans = ""

        while n != 0:
            digit = n % 10
            n /= 10
            if prev == digit:
                total += 1
            else:
                if prev != -1:
                    ans = str(total) + str(prev) + ans

                prev = digit
                total = 1

        if prev != -1:
            ans = str(total) + str(prev) + ans

        ans = int(ans)
        return ans 
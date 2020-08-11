class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for char in s:
            ans *= 26
            ans += ord(char) - ord('A') + 1

        return ans

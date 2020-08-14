from collections import defaultdict

class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniques = 0
        pairs = 0
        letters = defaultdict(int)
        for char in s:
            letters[char] += 1
            if letters[char] % 2 == 0:
                pairs += 1
                uniques -= 1
            else:
                uniques += 1

        ans = 1 if uniques > 0 else 0
        ans += pairs * 2
        return ans

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_char = {}
        longest = 0
        start = 0
        for index, char in enumerate(s):
            if char in last_char and last_char[char] >= start:
                longest = max(longest, index - last_char[char], index - start)
                start = last_char[char] + 1
            
            last_char[char] = index
        
        return max(longest, len(s) - start)
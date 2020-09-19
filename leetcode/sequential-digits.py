class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans = []

        for digits in range(2,11):
            for combos in range(0, 10-digits):
                string = ['']*digits
                for i in range(1+combos,digits+combos+1):
                    string[i-combos-1] = str(i)
                
                string = ''.join(string)

                num = int(string)
                if not (num < low):
                    if num > high:
                        return ans
                    
                    ans.append(num)
                
        return ans
                


                
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(A)-1
        while left < right:
            while left < right and A[left] % 2 == 0:
                left += 1
                
            while left < right and A[right] % 2 == 1:
                right -= 1
            
            if left < right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        return A

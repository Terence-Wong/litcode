import bisect
from collections import defaultdict

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """

        times = []
        change = defaultdict(int)

        for trip in trips:
            if not trip[1] in change:
                bisect.insort(times, trip[1])
            
            if not trip[2] in change:
                bisect.insort(times, trip[2])
                
            change[trip[1]] += trip[0]
            change[trip[2]] -= trip[0]
        
        cur = 0
        for time in times:
            cur += change[time]
            if cur > capacity:
                return False

        return True

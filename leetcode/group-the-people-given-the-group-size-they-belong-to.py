from collections import defaultdict

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groupData = defaultdict(list)
        for index, groupAssigned in enumerate(groupSizes):
            groupData[groupAssigned].append(index)
        
        result = []
        for groupType, people in groupData.items():
            index = 0
            while index < len(people):
                group = []
                for i in xrange(0, groupType):
                    group.append(people[index])
                    index = index + 1
                
                result.append(group)

        return result


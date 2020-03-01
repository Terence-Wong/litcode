class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.changes = {}
        self.history = []
        self.snapID = -1


    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.changes[index] = val
        

    def snap(self):
        """
        :rtype: int
        """
        self.history.append(self.changes)
        self.changes = {}
        self.snapID += 1 
        return self.snapID


    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        for time in range(snap_id, -1, -1):
            if index in self.history[time]:
                return self.history[time][index]
            
        return 0        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
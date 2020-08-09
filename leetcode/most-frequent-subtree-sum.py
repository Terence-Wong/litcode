# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def handleSum(sumAmount):
            self.frequencies[sumAmount] += 1
            if self.frequencies[sumAmount] == self.highest_freq:
                self.result.append(sumAmount)
            elif self.frequencies[sumAmount] > self.highest_freq:
                self.highest_freq = self.frequencies[sumAmount]
                self.result = [sumAmount]

        def evaluate(node):
            if node.left != None:
                evaluate(node.left)
                node.val += node.left.val
            if node.right != None:
                evaluate(node.right)
                node.val += node.right.val
            handleSum(node.val)

        self.highest_freq = 0
        self.frequencies = defaultdict(int)
        self.result = []
        if root == None:
            return []

        evaluate(root)
        return self.result
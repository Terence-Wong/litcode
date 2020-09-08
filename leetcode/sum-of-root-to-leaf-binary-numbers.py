# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sum(self, num, node):
        if not node:
            return num
        
        num *= 2
        num += node.val

        if not node.left and not node.right:
            return num

        ans = 0
        if node.left:
            ans += self.sum(num, node.left)
            
        if node.right:
            ans += self.sum(num, node.right)

        return ans


    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.sum(0, root) 

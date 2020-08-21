# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
            
        array = []
        cur = head
        while cur:
            array.append(cur)
            cur = cur.next
        
        left = 0
        right = len(array)-1
        leftTurn = True
        cur = head
        while left < right:
            if leftTurn:
                cur.next = array[right]
                cur = array[right]
                left += 1
            else:
                cur.next = array[left]
                cur = array[left]                
                right -= 1

            leftTurn = not leftTurn

        cur.next = None

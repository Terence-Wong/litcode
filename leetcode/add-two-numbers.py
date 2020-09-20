# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ans = ListNode() # init empty
        cur = ans
        carry = 0

        while l1 or l2 or carry:
            cur.next = ListNode()
            cur = cur.next

            a = 0
            b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            
            if l2:
                b = l2.val
                l2 = l2.next

            total = a + b + carry
            cur.val = total % 10 
            carry = (1 if total > 9 else 0)

        return ans.next
    
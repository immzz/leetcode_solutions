# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hA,hB = headA,headB
        jumpedA,jumpedB = False,False
        while hA and hB:
            if hA.val == hB.val:
                return hA
            hA,hB = hA.next,hB.next
            if not hA and not jumpedA:
                hA = headB
                jumpedA = True
            if not hB and not jumpedB:
                hB = headA
                jumpedB = True
            
            
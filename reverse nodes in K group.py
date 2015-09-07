# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        next_head = head
        s = []
        i = 0
        while i < k and next_head:
            s.append(next_head)
            next_head = next_head.next
            i += 1
        if len(s) == k:
            dummy = ListNode(None)
            current = dummy
            while s:
                current.next = s.pop()
                current.next.next = None
                current = current.next
            current.next = self.reverseKGroup(next_head,k)
            return dummy.next
        else:
            return head
        
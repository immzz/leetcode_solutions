# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        i = 1
        s = []
        dummy = ListNode(None)
        dummy.next = head
        current,prev = head,dummy
        while current:
            if i < m:
                prev = current
                current = current.next
            if i >= m and i <= n:
                s.append(current)
                current = current.next
            if i == n:
                while s:
                    prev.next = s.pop()
                    prev.next.next = None
                    prev = prev.next
                prev.next = current
                break
            i += 1
        return dummy.next
                
                    
        
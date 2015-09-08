# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        candidate_prev = dummy
        candidate = head
        count = 0
        while candidate:
            prev = dummy
            for i in xrange(count):
                if candidate.val < prev.next.val:
                    break
                prev = prev.next
            if prev == candidate_prev:
                candidate_prev = candidate
                candidate = candidate.next
                count += 1
                continue
            candidate_prev.next = candidate.next
            candidate.next = prev.next
            prev.next = candidate
            candidate = candidate_prev.next
            count += 1
        return dummy.next
                
                
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(4)

sol = Solution()
sol.insertionSortList(head)
         
            

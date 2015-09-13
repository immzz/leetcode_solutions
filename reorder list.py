# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        current = head
        s = []
        count = 0
        while current:
            s.append(current)
            count += 1
            current = current.next
        current_head = head
        for _ in xrange(count/2):
            next = current_head.next
            current_head.next = s.pop()
            current_head.next.next = next
            current_head = next
        current_head.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
sol = Solution()
sol.reorderList(head)
print head.val,head.next.val,head.next.next.val,head.next.next.next.val,head.next.next.next.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        if not head.next:
            return head
        prev,current = head,head.next
        while current.next:
            prev = current
            current = current.next
        if prev == head:
            
            return head
        prev.next = None
        next = head.next
        head.next = current
        current.next = self.reorderList(next)
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
sol = Solution()
sol.reorderList(head)
print head.val,head.next.val,head.next.next.val,head.next.next.next.val,head.next.next.next.next
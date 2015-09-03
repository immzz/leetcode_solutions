# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head:
            return None
        left_dummy = ListNode(None)
        right_dummy = ListNode(None)
        equal_dummy = ListNode(None)
        left_current = left_dummy
        right_current = right_dummy
        equal_current = equal_dummy
        while head:
            next = head.next
            if head.val < x:
                left_current.next = head
                left_current = head
            else:
                right_current.next = head
                right_current = head
            head = next
        new_head = None
        new_tail = None
        if not new_head and left_dummy.next:
            new_head = left_dummy.next
            new_tail = left_current
        if not new_head and right_dummy.next:
            new_head = right_dummy.next
            new_tail = right_current
        elif right_dummy.next:
            new_tail.next = right_dummy.next
            new_tail = right_current
        if new_tail:
            new_tail.next = None
        return new_head
        
        
        
head = ListNode(1)
head.next = ListNode(2)
sol = Solution()
sol.partition(head,1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        next = head.next
        next_next = head.next.next
        head.next = None
        while next:
            next.next = head
            head = next
            next = next_next
            if next_next:
                next_next = next_next.next
        return head
            
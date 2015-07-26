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
        new_head = self.reverseList(head.next)
        if new_head:
            head.next.next = head
            head.next = None
            return new_head
        else:
            head.next = None
            return head
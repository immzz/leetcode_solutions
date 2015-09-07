# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        current,prev = head,dummy
        duplicate = False
        while current:
            if not current.next:
                break
            if current.next.val == current.val:
                current.next = current.next.next
                duplicate = True
            else:
                if duplicate:
                    prev.next = prev.next.next
                    current = prev.next
                    duplicate = False
                else:
                    prev = current
                    current = current.next
        if duplicate:
                prev.next = prev.next.next
        return dummy.next
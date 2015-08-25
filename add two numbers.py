# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 and l2:
            sum = carry + l1.val + l2.val
            current.next = ListNode(sum%10)
            carry = sum/10
            current = current.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = carry + l1.val
            current.next = ListNode(sum%10)
            carry = sum/10
            current = current.next
            l1 = l1.next
        while l2:
            sum = carry + l2.val
            current.next = ListNode(sum%10)
            carry = sum/10
            current = current.next
            l2 = l2.next
        if carry:
            current.next = ListNode(carry)
        return dummy.next
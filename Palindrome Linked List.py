# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head:
            return True
        if not head.next:
            return True
        #find middle
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = slow if not fast else slow.next
        #reverse first half
        current = head
        next = head.next
        head.next = None
        while not (next == slow):
            next_next = next.next
            next.next = current
            current = next
            next = next_next
        while current and second_half:
            if not (current.val == second_half.val):
                return False
            current = current.next
            second_half = second_half.next
        return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(1)


sol = Solution()
print sol.isPalindrome(head)
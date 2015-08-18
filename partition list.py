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
        left_end = None
        xnode = head
        less_count = 0
        while xnode:
            if xnode.val < x:
                less_count += 1
            xnode = xnode.next
        print less_count
        if less_count == 0:
            return head
        xnode = head
        for i in xrange(less_count):
            xnode = xnode.next
        print xnode.val
        left = head
        right = xnode
        while True:
            while left != xnode and left.val < x:
                left = left.next
            while right and right.val >= x:
                right = right.next
            if (left == xnode) or (not right):
                break
            print left.val,right.val
            temp = left.val
            left.val = right.val
            right.val = temp
        return head

head = ListNode(2)
head.next = ListNode(3)
head.next.next = ListNode(1)

sol = Solution()
head = sol.partition(head,2)
print head.val,head.next.val
        
        
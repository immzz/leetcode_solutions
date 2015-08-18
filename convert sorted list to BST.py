# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        fast = head
        slow = head
        temp = None
        while fast.next and fast.next.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
        if temp:
            temp.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head) if temp else None
        root.right = self.sortedListToBST(slow.next)
        return root

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
#head.next.next = ListNode(3)
#head.next.next.next = ListNode(4)
root = sol.sortedListToBST(head)
print root.val,root.left,root.right.val
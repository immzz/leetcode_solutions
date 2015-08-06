# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

'''
        1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
  /           \
8     ->       9 -> NULL
'''

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        while root:
            next_root = None
            left = None
            right = None
            while root:
                if not next_root:
                    next_root = root.left if root.left else root.right
                if root.left:
                    if not left:
                        left = root.left
                    elif not right:
                        right = root.left
                if left and right:
                    left.next = right
                    left = right
                    right = None
                if root.right:
                    if not left:
                        left = root.right
                    elif not right:
                        right = root.right
                if left and right:
                    left.next = right
                    left = right
                    right = None
                root = root.next
            root = next_root
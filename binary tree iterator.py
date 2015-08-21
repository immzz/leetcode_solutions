# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = []
        while root:
            self.s.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.s) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.s.pop()
        if node.right:
            current = node.right
            while current:
                self.s.append(current)
                current = current.left
        return node.val

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
# Your BSTIterator will be called like this:
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
print [x.val for x in v]
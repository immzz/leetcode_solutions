# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root == None:
            return []
        else:
            return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
    def preorderIterativelyTraveral(self,root):
        result = []
        node_stack = [root]
        counter_stack = [0]
        while node_stack:
            counter_stack[-1] = counter_stack[-1] + 1
            if node_stack[-1] == None or counter_stack[-1] == 3:
                node_stack.pop()
                counter_stack.pop()
            elif counter_stack[-1] == 1:
                result = result + [node_stack[-1].val]
                node_stack.append(node_stack[-1].left)
                counter_stack.append(0)
            elif counter_stack[-1] == 2:
                node_stack.append(node_stack[-1].right)
                counter_stack.append(0)
        return result
    def postorderIterativelyTraveral(self,root):
        result = []
        node_stack = [root]
        counter_stack = [0]
        while node_stack:
            counter_stack[-1] = counter_stack[-1] + 1
            if node_stack[-1] == None:
                node_stack.pop()
                counter_stack.pop()
            elif counter_stack[-1] == 3:
                result = result + [node_stack.pop().val]
                counter_stack.pop()
            elif counter_stack[-1] == 1:
                node_stack.append(node_stack[-1].left)
                counter_stack.append(0)
            elif counter_stack[-1] == 2:
                node_stack.append(node_stack[-1].right)
                counter_stack.append(0)
        return result
    def inorderIterativelyTraveral(self,root):
        result = []
        node_stack = [root]
        counter_stack = [0]
        while node_stack:
            counter_stack[-1] = counter_stack[-1] + 1
            if node_stack[-1] == None or counter_stack[-1] == 3:
                node_stack.pop()
                counter_stack.pop()
            elif counter_stack[-1] == 1:
                node_stack.append(node_stack[-1].left)
                counter_stack.append(0)
            elif counter_stack[-1] == 2:
                result = result + [node_stack[-1].val]
                node_stack.append(node_stack[-1].right)
                counter_stack.append(0)
        return result
            
            
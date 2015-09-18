class TreeNode(object):
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
    
def longestSequence(root,res):
    if not root:
        return [0,0]
    starting_here,ending_here = 1,1
    starting_left,ending_left = longestSequence(root.left,res)
    starting_right,ending_right = longestSequence(root.right,res)
    if root.left and root.left.val == root.val + 1:
        starting_here = max(starting_here,starting_left+1)
    elif root.left and root.left.val == root.val - 1:
        ending_here = max(ending_here,ending_left+1)
    if root.right and root.right.val == root.val + 1:
        starting_here = max(starting_here,starting_right+1)
    elif root.right and root.right.val == root.val - 1:
        ending_here = max(ending_here,ending_right+1)
    res[0] = max(res[0],starting_here,ending_here)
    if root.left and root.right:
        if root.right.val == root.val - 1 and root.left.val == root.val + 1:
            res[0] = max(res[0],ending_right+1+starting_left)
        elif root.right.val == root.val + 1 and root.left.val == root.val - 1:
            res[0] = max(res[0],ending_left+1+starting_right)
    return [starting_here,ending_here]

root = TreeNode(1)

root.left = TreeNode(2)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.left.left = TreeNode(3)

res = [0]
longestSequence(root,res)
print res[0]
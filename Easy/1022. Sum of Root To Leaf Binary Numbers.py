# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        if root is None:
            return 0
        stack = [(root, str(root.val))]
        while stack:
            v, s = stack.pop()
            if v:
                if not v.left and not v.right:
                    result += int(s, 2)
                if v.left:
                    stack.append((v.left, s + str(v.left.val)))
                if v.right:
                    stack.append((v.right, s + str(v.right.val)))
        return result
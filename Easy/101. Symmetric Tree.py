from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isSym(root.left, root.right)

    def isSym(self, leftroot, rightroot):
        if leftroot is None and rightroot is None:
            return True
        if leftroot is None or rightroot is None:
            return False
        if leftroot.val != rightroot.val:
            return False
        return self.isSym(leftroot.left, rightroot.right) and self.isSym(leftroot.right, rightroot.left)
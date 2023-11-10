from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sums = 0
        def solve(root):
            if root is None:
                return 0
            l = solve(root.left)
            r= solve(root.right)
            self.sums = self.sums + abs(l-r)
            return l+ r + root.val
        solve(root)
        return self.sums
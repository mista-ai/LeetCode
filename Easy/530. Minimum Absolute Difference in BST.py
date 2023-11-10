# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root) -> int:
        self.prev = float('inf')
        def dfs(root, min_diff):
            if not root:
                return min(float('inf'), min_diff)
            min_diff = dfs(root.left, min_diff)
            min_diff = min(min_diff, abs(self.prev - root.val))
            self.prev = root.val
            min_diff = dfs(root.right, min_diff)
            return min_diff

        return dfs(root, float('inf'))
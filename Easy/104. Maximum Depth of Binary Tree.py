from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        search = deque([(0, root)])
        while search:
            d, v = search.popleft()
            if v:
                search.append((d + 1, v.left))
                search.append((d + 1, v.right))
        return d
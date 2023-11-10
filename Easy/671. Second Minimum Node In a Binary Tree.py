from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        counter = 0
        search = deque([root])
        min_val = float('inf')
        while search:
            vertice = search.popleft()
            if vertice:
                if vertice.val > root.val and vertice.val < min_val:
                    min_val = vertice.val
                search.append(vertice.left)
                search.append(vertice.right)
        if min_val == float('inf'):
            return -1
        else:
            return min_val
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        search = deque([root])
        values = list()
        while search:
            level = list()
            levellen = len(search)
            for i in range(levellen):
                node = search.popleft()
                if node:
                    level.append(node.val)
                    search.append(node.left)
                    search.append(node.right)
            if level:
                values.append(level)
        return values
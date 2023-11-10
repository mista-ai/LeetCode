from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        x = root.val
        search_queue = deque()
        search_queue.append(root)
        while search_queue:
            vertice = search_queue.popleft()
            if vertice is not None:
                if vertice.val != x:
                    return False
                search_queue.append(vertice.left)
                search_queue.append(vertice.right)
        return True
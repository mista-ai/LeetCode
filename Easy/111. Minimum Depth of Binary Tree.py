from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        search_queue = deque()
        if root.left is not None:
            search_queue.append((2, root.left))
        if root.right is not None:
            search_queue.append((2, root.right))
        while search_queue:
            node = search_queue.popleft()
            if node[1].left is None and node[1].right is None:
                return node[0]
            if node[1].left is not None:
                search_queue.append((node[0] + 1, node[1].left))
            if node[1].right is not None:
                search_queue.append((node[0] + 1, node[1].right))
        return 1
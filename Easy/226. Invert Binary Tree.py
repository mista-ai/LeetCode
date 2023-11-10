# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        search_queue = deque()
        search_queue.append(root)
        while search_queue:
            vertice = search_queue.popleft()
            vertice.left, vertice.right = vertice.right, vertice.left
            if vertice.right is not None:
                search_queue.append(vertice.right)
            if vertice.left is not None:
                search_queue.append(vertice.left)
        return root
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        search_queue = deque()
        search_queue.append((0, root, None))
        x_data = None
        y_data = None
        while search_queue:
            depth, vertice, parent = search_queue.popleft()
            if vertice is not None:
                if vertice.val == x:
                    x_data = (parent.val, depth)
                if vertice.val == y:
                    y_data = (parent.val, depth)
                search_queue.append((depth + 1, vertice.left, vertice))
                search_queue.append((depth + 1, vertice.right, vertice))
            if x_data is not None and y_data is not None:
                if x_data[0] != y_data[0] and x_data[1] == y_data[1]:
                    return True
                else:
                    return False

        return False
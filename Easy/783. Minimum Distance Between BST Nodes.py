from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def most_right_for_left(self, root):
        root_val = root.val
        root = root.left
        while root.right:
            root = root.right
        return root_val - root.val

    def most_left_for_right(self, root):
        root_val = root.val
        root = root.right
        while root.left:
            root = root.left
        return root.val - root_val

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        search = deque()
        search.append(root)
        while search:
            vertice = search.popleft()
            if vertice.left is not None:
                search.append(vertice.left)
                diff = self.most_right_for_left(vertice)
                if diff < min_diff:
                    min_diff = diff
            if vertice.right is not None:
                search.append(vertice.right)
                diff = self.most_left_for_right(vertice)
                if diff < min_diff:
                    min_diff = diff
        return min_diff
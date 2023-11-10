from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        root2 = TreeNode(None, None, None)
        current = root2
        search = deque()
        vertice = root
        prev = None
        while vertice or search:
            while vertice:
                search.append(vertice)
                vertice = vertice.left
            vertice = search.pop()
            prev = current
            current.val = vertice.val
            current.right = TreeNode(None, None, None)
            current = current.right
            vertice = vertice.right
        prev.right = None
        return root2

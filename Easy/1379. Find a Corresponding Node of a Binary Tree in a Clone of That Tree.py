from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        search_o = deque()
        search_c = deque()
        search_o.append(original)
        search_c.append(cloned)
        while search_o:
            vertice_o = search_o.popleft()
            vertice_c = search_c.popleft()
            if vertice_o == target:
                return vertice_c
            if vertice_o is not None:
                search_o.append(vertice_o.left)
                search_o.append(vertice_o.right)
                search_c.append(vertice_c.left)
                search_c.append(vertice_c.right)
        return None
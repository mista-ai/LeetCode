from collections import deque, defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        search = deque()
        search.append(root)
        hash_table = defaultdict(int)
        while search:
            vertice = search.popleft()
            if vertice:
                if vertice.val * 2 != k:
                    hash_table[vertice.val] = k - vertice.val
                search.append(vertice.left)
                search.append(vertice.right)
                if (k - vertice.val) in hash_table:
                    return True

        for key, val in hash_table.items():
            if val in hash_table:
                return True
        return False

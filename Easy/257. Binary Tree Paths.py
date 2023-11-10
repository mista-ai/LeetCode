from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = list()
        if not root:
            return result
        search = deque([(f'{root.val}', root)])
        while search:
            path, v = search.pop()
            if v:
                if v.left is None and v.right is None:
                    result.append(path)
                if v.right:
                    search.append((f'{path}->{v.right.val}', v.right))
                if v.left:
                    search.append((f'{path}->{v.left.val}', v.left))
        return result
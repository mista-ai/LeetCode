# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if root is None:
                return ''
            result = str(root.val)
            if root.left is not None:
                result += f'({dfs(root.left)})'
            if root.left is None and root.right is not None:
                result += '()'
            if root.right is not None:
                result += f'({dfs(root.right)})'
            return result
        return dfs(root)
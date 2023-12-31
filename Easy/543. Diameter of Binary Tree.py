# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.big = 0
        def postorder(root):
            if not root:
                return 0
            left = postorder(root.left)
            right = postorder(root.right)
            self.big = max(left + right, self.big)
            return max(left, right) + 1
        postorder(root)
        return self.big
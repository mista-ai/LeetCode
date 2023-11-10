# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def postorder(root):
            if root.val == 2:
                return postorder(root.left) or postorder(root.right)
            elif root.val == 3:
                return postorder(root.left) and postorder(root.right)
            else:
                return root.val
        return postorder(root)
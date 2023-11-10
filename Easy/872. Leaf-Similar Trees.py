# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def postorder(root):
            if not root:
                return
            list1 = []
            left = postorder(root.left)
            right = postorder(root.right)
            if left == None and right == None:
                list1.append(root.val)
            if left:
                list1.extend(left)
            if right:
                list1.extend(right)
            return list1
        return postorder(root1) == postorder(root2)
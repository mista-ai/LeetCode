# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def createString(node):
           if not node: return "n"
           return f'|{node.val},{createString(node.left)},{createString(node.right)}'
        a = createString(root)
        b = createString(subRoot)

        return b in a
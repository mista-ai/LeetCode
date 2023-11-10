from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def cal_depth(root):
            cnt = 0
            p = root
            while p:
                p = p.left
                cnt += 1
            return cnt

        def count_nodes(root):
            if not root:
                return 0
            ld = cal_depth(root.left)
            rd = cal_depth(root.right)
            # print(ld,rd)
            if ld == rd:
                return 1 + count_nodes(root.right) + 2 ** ld - 1
            elif ld == rd + 1:
                return 1 + count_nodes(root.left) + 2 ** rd - 1
            else:
                assert False

        return count_nodes(root)
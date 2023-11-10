from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        search_queue = deque()
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        if root.left is not None:
            search_queue.append((root.val + root.left.val, root.left))
        if root.right is not None:
            search_queue.append((root.val + root.right.val, root.right))
        while search_queue:
            cur_sum, cur_node = search_queue.popleft()
            if cur_node.left is None and cur_node.right is None and cur_sum == targetSum:
                return True
            if cur_node.left is not None:
                search_queue.append((cur_sum + cur_node.left.val, cur_node.left))
            if cur_node.right is not None:
                search_queue.append((cur_sum + cur_node.right.val, cur_node.right))
        return False
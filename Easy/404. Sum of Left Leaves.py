# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 0
            search_queue = deque()
            result = 0
            if root.left is not None:
                search_queue.append((True, root.left))
            if root.right is not None:
                search_queue.append((False, root.right))
            while search_queue:
                left, cur_node = search_queue.popleft()
                if cur_node.left is None and cur_node.right is None and left:
                    result += cur_node.val
                    continue
                if cur_node.left is not None:
                    search_queue.append((True, cur_node.left))
                if cur_node.right is not None:
                    search_queue.append((False, cur_node.right))
            return result
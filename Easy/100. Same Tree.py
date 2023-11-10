from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        if p.val != q.val:
            return False
        search_queue_p = deque()
        search_queue_q = deque()
        search_queue_p.append(p.left)
        search_queue_p.append(p.right)
        search_queue_q.append(q.left)
        search_queue_q.append(q.right)
        while search_queue_p and search_queue_q:
            vertice_p = search_queue_p.popleft()
            vertice_q = search_queue_q.popleft()
            if vertice_p is None:
                if vertice_q is not None:
                    return False
                continue
            if vertice_q is None:
                if vertice_p is not None:
                    return False
                continue
            if vertice_p.val != vertice_q.val:
                return False
            search_queue_p.append(vertice_p.left)
            search_queue_p.append(vertice_p.right)
            search_queue_q.append(vertice_q.left)
            search_queue_q.append(vertice_q.right)
        return True
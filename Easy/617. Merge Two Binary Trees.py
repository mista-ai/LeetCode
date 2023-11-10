# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        search_queue1 = deque()
        search_queue1.append(root1)
        search_queue2 = deque()
        search_queue2.append(root2)
        while search_queue1 or search_queue2:
            vertice1 = search_queue1.popleft()
            vertice2 = search_queue2.popleft()
            vertice1.val += vertice2.val
            if vertice1.left is None:
                vertice1.left = vertice2.left
            elif vertice2.left is not None:
                search_queue1.append(vertice1.left)
                search_queue2.append(vertice2.left)
            if vertice1.right is None:
                vertice1.right = vertice2.right
            elif vertice2.right is not None:
                search_queue1.append(vertice1.right)
                search_queue2.append(vertice2.right)

        return root1
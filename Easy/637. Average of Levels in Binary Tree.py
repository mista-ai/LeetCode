from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sum_of_level = 0
        counter_of_level = 0
        if root is None:
            return [0]
        sums = list()
        last_depth = 0
        search = deque()
        search.append((0, root))
        while search:
            depth, vertice = search.popleft()
            if vertice is not None:
                if depth != last_depth:
                    sums.append(sum_of_level / counter_of_level)
                    last_depth = depth
                    sum_of_level = 0
                    counter_of_level = 0
                counter_of_level += 1
                sum_of_level += vertice.val
                search.append((depth + 1, vertice.left))
                search.append((depth + 1, vertice.right))
        sums.append(sum_of_level / counter_of_level)
        return sums
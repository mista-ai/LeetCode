"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        s = deque()

        s.append((1, root))
        maxdepth = 0
        while s:
            depth, v = s.popleft()
            if depth > maxdepth:
                maxdepth = depth
            if v is not None:
                for x in v.children:
                    s.append((depth + 1, x))
        return maxdepth
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = set(edges[0])
        second = set(edges[1])
        return (first & second).pop()
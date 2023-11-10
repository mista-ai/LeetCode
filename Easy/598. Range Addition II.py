class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        ops.append([m, n])
        return min(e[0] for e in ops) * min(e[1] for e in ops)
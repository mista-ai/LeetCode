class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set(candyType)
        allowed = len(candyType) // 2
        if len(types) > allowed:
            return allowed
        else:
            return len(types)
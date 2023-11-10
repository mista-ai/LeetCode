class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = dict()
        nums = sorted(list(set(arr)))
        for i in range(len(nums)):
            ranks[nums[i]] = i + 1
        result = list()
        for x in arr:
            result.append(ranks[x])
        return result
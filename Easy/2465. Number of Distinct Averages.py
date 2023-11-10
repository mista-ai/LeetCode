class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        result = set()
        nums.sort()
        while nums:
            result.add(nums[0] + nums[-1])
            del nums[0]
            del nums[-1]
        return len(result)
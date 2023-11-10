class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = list()
        l = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if i - l == 1:
                    result.append(f"{nums[l]}")
                    l = i
                else:
                    result.append(f"{nums[l]}->{nums[i - 1]}")
                    l = i
        if l < len(nums):
            if len(nums) - l == 1:
                result.append(f"{nums[l]}")
            else:
                result.append(f"{nums[l]}->{nums[len(nums) - 1]}")
        return result

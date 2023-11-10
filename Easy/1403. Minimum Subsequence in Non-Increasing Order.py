class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        result = list()
        result_sum = 0
        total = sum(nums)
        for x in nums:
            result_sum += x
            result.append(x)
            if result_sum > total - result_sum:
                return result
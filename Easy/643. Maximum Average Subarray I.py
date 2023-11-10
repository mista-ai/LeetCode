class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        n = len(nums)
        left = 0
        right = 1 + k - 1
        while right < n:
            cur_sum = cur_sum - nums[left] + nums[right]
            if max_sum < cur_sum:
                max_sum = cur_sum
            left += 1
            right += 1
        return max_sum / k
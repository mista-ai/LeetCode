class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        begin = 0
        end = len(nums) - 1
        while begin < end:
            mid = (begin + end) // 2
            if nums[mid] != mid:
                end = mid - 1
            else:
                begin = mid + 1
        if nums[begin] == begin:
            return begin + 1
        else:
            return begin
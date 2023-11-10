class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = [None] * len(nums)
        counter = len(nums) - 1
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                result[counter] = nums[left] * nums[left]
                left += 1
            else:
                result[counter] = nums[right] * nums[right]
                right -= 1
            counter -= 1
        return result
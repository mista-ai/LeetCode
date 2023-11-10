class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums)/2

        for num in set(nums):
            if nums.count(num) > major:
                return num
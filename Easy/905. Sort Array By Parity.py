# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         l = 0
#         r = len(nums) - 1
#         while l < r:
#             if nums[l] % 2 == 1:
#                 while l < r:
#                     if nums[r] % 2 == 0:
#                         nums[l], nums[r] = nums[r], nums[l]
#                         r -= 1
#                         break
#                     r -= 1
#             l += 1
#         return nums

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        cnt = 0
        for i in range(len(nums)):
            if not nums[i] % 2:
                nums[i], nums[cnt] = nums[cnt], nums[i]
                cnt += 1
        return nums

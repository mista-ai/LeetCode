# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         result = list()
#         for i in range(len(nums)):
#             counter = 0
#             for j in range(len(nums)):
#                 if nums[i] > nums[j]:
#                     counter += 1
#             result.append(counter)
#         return result

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        mapping = {}
        result = []
        for i in range(len(temp)):
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        for i in range(len(nums)):
            result.append(mapping[nums[i]])
        return result

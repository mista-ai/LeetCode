class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                i += 1
            else:
                nums[j] = nums[i]
                j += 1
                i += 1
        return j
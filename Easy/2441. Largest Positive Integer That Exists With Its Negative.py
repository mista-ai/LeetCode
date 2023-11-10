class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        z = set()
        y = []
        for i in range(len(nums)):
            z.add(nums[i])
        for j in z:
            if j and -j in z:
                y.append(j)
        if y == []:
            return -1
        else:
            return max(y)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        tmp = 0
        for d in nums:
            if d == 1:
                tmp += 1
            else:
                consec = max(tmp, consec)
                tmp = 0
        consec = max(tmp, consec)
        return consec
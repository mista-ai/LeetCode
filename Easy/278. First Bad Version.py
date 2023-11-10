# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        begin = 1
        end = n
        while begin <= end:
            mid = (begin + end) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                begin = mid + 1
        return begin
from math import floor
from math import sqrt

class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2
            asum = (mid+1) * mid // 2
            if asum == n:
                return mid
            elif asum > n:
                end = mid - 1
            else:
                start = mid + 1
        return end
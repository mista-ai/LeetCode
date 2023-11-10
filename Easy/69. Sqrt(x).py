class Solution:
    def mySqrt(self, x: int) -> int:
            if x == 0:
                return x
            begin = 1
            end = x
            while begin <= end:
                mid = begin + (end - begin) // 2
                if mid > x // mid:
                    end = mid - 1
                elif mid == x // mid:
                    return mid
                else:
                    begin = mid + 1
            return end
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            if not n % 3:
                n //= 3
                continue
            return False
        return True
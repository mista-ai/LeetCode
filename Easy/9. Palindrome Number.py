class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        t = x
        while t > 0:
            reverse *= 10
            reverse += t % 10
            t //= 10
        return x == reverse
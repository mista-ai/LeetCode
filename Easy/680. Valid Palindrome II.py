class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        count = 0
        if s == s[::-1]: return True
        while left < right:
            first, second = s[left], s[right]
            if first == second:
                left += 1
                right -= 1
            else:
                new1 = s[0:left] + s[left + 1:]
                new2 = s[0:right] + s[right + 1:]
                if new1 == new1[::-1]:
                    return True
                elif new2 == new2[::-1]:
                    return True
                else:
                    return False
        return True


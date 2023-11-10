class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            sl, sr = s[l - 1:r], s[l:r]
            if l - 1 >= 0 and sl == sl[::-1]:
                start, size = l - 1, size + 2
            elif sr == sr[::-1]:
                start, size = l, size + 1
        return s[start:start + size]
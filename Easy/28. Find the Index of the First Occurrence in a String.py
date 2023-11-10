class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        r = 0
        length = len(haystack)
        nl = len(needle)
        while l + r < length:
            if haystack[l + r] == needle[r]:
                r += 1
            else:
                r = 0
                l += 1
            if r == nl:
                return l

        return -1
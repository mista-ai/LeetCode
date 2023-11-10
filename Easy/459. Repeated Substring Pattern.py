class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        if length < 2:
            return False
        for i in range(length // 2):
            if length % (i + 1) == 0 and s[:i+1] * (length // (i + 1)) == s:
                return True
        return False
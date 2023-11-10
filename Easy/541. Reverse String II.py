class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s[::-1]
        elif len(s) < 2*k:
            return s[:k][::-1] + s[k:]
        result = ''
        for i in range(0, len(s), 2 * k):
            result += s[i:i+k][::-1] + s[i+k:i+2*k]
        return result
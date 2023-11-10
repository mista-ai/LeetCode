class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)//2):
            if s[i] > s[-i-1]:
                s[i] = s[-i-1]
            elif s[i] < s[-i-1]:
                s[-i-1] = s[i]
        return ''.join(s)
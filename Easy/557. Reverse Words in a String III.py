class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split()
        for i in range(len(result)):
            result[i] = result[i][::-1]
        return ' '.join(result)
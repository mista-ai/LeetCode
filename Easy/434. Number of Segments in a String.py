class Solution:
    def countSegments(self, s: str) -> int:
        counter = 0
        p = 0
        in_word = False
        while p < len(s):
            if s[p] == ' ':
                in_word = False
            else:
                if not in_word:
                    counter += 1
                in_word = True
            p += 1
        return counter
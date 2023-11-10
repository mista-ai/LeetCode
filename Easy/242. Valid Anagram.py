class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        min_word = s
        max_word = t
        if len(min_word) > len(max_word):
            min_word, max_word = max_word, min_word
        letters_s = dict()
        for x in min_word:
            if x in letters_s:
                letters_s[x] += 1
            else:
                letters_s[x] = 1
        for x in max_word:
            if x not in letters_s:
                return False
            else:
                letters_s[x] -= 1
                if letters_s[x] < 0:
                    return False
        return True
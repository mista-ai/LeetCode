from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dict = Counter(s)
        result = 0
        flag = True
        for val in s_dict.values():
            if val % 2 == 0:
                result += val
            else:
                if flag:
                    flag = False
                    result += 1
                result += val - 1
        return result
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)
        for l in t:
            if l not in s_dict or t_dict[l] > s_dict[l]:
                return l
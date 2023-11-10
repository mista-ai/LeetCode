class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_t = dict()
        s = s.split()
        if len(set(pattern)) != len(set(s)) or len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in hash_t:
                hash_t[pattern[i]] = s[i]
            elif hash_t[pattern[i]] != s[i]:
                return False
        return True
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        letters = dict()
        s = list(s)
        swap = False
        can_be = False
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = 1
            else:
                letters[s[i]] += 1

            if s[i] != goal[i] and swap is False:
                for j in range(i+1, len(s)):
                    if goal[j] == s[i] and goal[i] == s[j]:
                        s[i], s[j] = s[j], s[i]
                        break
                swap = True
            if swap is True and s[i] != goal[i]:
                return False
        can_be = any(x >= 2 for x in letters.values())

        return swap or can_be
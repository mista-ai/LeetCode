class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        cs = list()
        n = len(s)
        for i in range(n):
            if s[i] == c:
                cs.append(i)
        left = -1
        right = 0
        result = list()
        for i in range(n):
            if s[i] == c:
                result.append(0)
                left += 1
                right += 1
            elif i < cs[0]:
                result.append(cs[0] - i)
            elif i > cs[-1]:
                result.append(i - cs[-1])
            else:
                dist = min(i - cs[left], cs[right] - i)
                result.append(dist)

        return result
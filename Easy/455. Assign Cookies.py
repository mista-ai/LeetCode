class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        s = sorted(s)
        g = sorted(g)
        pos = 0
        lg = len(g)
        for cookie in s:
            if cookie >= g[pos]:
                ans +=1
                pos +=1
            if pos > (lg-1):
                break
        return(ans)
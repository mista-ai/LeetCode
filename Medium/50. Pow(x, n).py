class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        answer = 1
        pos = True if n > 0 else False
        if not pos:
            n = -n
        while n > 0:
            if n % 2 == 1:
                answer *= x
            x *= x
            n //= 2
        
        return answer if pos else 1 / answer
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        def find_divisors(n):
            result = 0
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    result += i
                    if i != n // i and i != 1:
                        result += n // i
            return result
        return num == find_divisors(num)
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sumx = 0
            while num:
                sumx += num % 10
                num = num // 10
            num = sumx
        return num
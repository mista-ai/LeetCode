class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        result = []
        sign = ''
        if num < 0:
            num *= -1
            sign = '-'
        while num > 0:
            result.append(str(num % 7))
            num //= 7
        return sign + ''.join(result[::-1])
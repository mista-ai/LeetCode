class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        hex_map = '0123456789abcdef'
        result = list()

        if num < 0:
            num += 0x100000000

        while num > 0:
            result.append(hex_map[num % 16])
            num //= 16

        return ''.join(result)[::-1]
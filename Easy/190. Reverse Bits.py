class Solution:
    def reverseBits(self, n: int) -> int:
        n = (bin(n)[2:].zfill(32))[::-1].lstrip('0')
        if n == '':
            return 0
        return int(n, 2)
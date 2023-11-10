class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        complement = []
        for x in num:
            if x == '1':
                complement.append('0')
            else:
                complement.append('1')
        return int(''.join(complement), 2)
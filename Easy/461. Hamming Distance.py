class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if y > x:
            y, x = x, y
        x = bin(x)[2:]
        y = bin(y)[2:]
        counter = 0
        i = 1
        while i <= len(x):
            if i > len(y) and x[-i] == '1':
                counter += 1
            elif i <= len(y) and x[-i] != y[-i]:
                counter += 1
            i += 1
        return counter
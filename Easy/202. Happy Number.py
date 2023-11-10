class Solution:
    def isHappy(self, n):
        squares = set()
        squares.add(n)
        while True:
            x = str(n)
            total = 0
            for digit in x:
                total += int(digit) ** 2
            if total == 1:
                return True
            elif total in squares:
                return False
            squares.add(total)
            n = total
        return False
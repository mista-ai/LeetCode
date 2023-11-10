class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(map(int, list(a)))[::-1]
        b = list(map(int, list(b)))[::-1]
        len_a = len(a)
        len_b = len(b)
        result = [0]
        i = 0
        while i < len_a or i < len_b:
            if i < len_a:
                result[i] += a[i]
            if i < len_b:
                result[i] += b[i]
            if result[i] > 1:
                result[i] %= 2
                result.append(1)
                i += 1
                continue
            i += 1
            if i < len_a or i < len_b:
                result.append(0)

        result = ''.join(map(str, result[::-1]))
        return result
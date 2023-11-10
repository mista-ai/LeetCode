class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        res = []
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            if j >= 0:
                carry += int(num2[j])
                j -= 1
            res.append(str(carry%10))
            carry = carry//10
        if carry:
            res.append(str(carry))
        return ''.join(res)[::-1]
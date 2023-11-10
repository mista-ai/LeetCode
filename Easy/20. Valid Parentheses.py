class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        paradict = {')': '(', '}': '{', ']': '['}
        for para in s:
            if para in '([{':
                stack.append(para)
            else:
                if len(stack) == 0 or paradict[para] != stack.pop():
                    return False
        if len(stack) != 0:
            return False
        return True
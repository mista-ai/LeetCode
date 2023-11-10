class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack, t_stack = list(), list()
        for x in s:
            if x != '#':
                s_stack.append(x)
            elif len(s_stack) > 0:
                s_stack.pop()
        for x in t:
            if x != '#':
                t_stack.append(x)
            elif len(t_stack) > 0:
                t_stack.pop()
        return t_stack == s_stack
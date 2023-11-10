class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_p = 0
        typed_p = 0
        if len(typed) < len(name):
            return False
        while name_p < len(name) or typed_p < len(typed):
            if name_p < len(name) and typed_p >= len(typed):
                return False
            if name_p < len(name) and name[name_p] == typed[typed_p]:
                name_p += 1
                typed_p += 1
            elif typed_p > 0 and typed[typed_p] == typed[typed_p - 1]:
                typed_p += 1
            else:
                return False
        return True
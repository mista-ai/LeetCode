class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        ok = set()
        for x in arr:
            if x in ok:
                return True
            ok.add(x * 2)
            ok.add(x / 2)
        return False
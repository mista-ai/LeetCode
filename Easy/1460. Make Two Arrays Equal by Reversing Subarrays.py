# class Solution:
#     def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
#         return sorted(target) == sorted(arr)

from collections import defaultdict

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(arr) != len(target):
            return False
        target_dict = defaultdict(int)
        arr_dict = defaultdict(int)
        for x in target:
            target_dict[x] += 1
        for x in arr:
            arr_dict[x] += 1
        for x in target:
            if target_dict[x] != arr_dict[x]:
                return False
        return True
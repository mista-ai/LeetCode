from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_freq = defaultdict(int)
        tail = list()
        for x in arr1:
            if x in arr2:
                arr2_freq[x] += 1
            else:
                tail.append(x)
        result = list()
        for x in arr2:
            result.extend([x] * arr2_freq[x])
        result.extend(sorted(tail))
        return result
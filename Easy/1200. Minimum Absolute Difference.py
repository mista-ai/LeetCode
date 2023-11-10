from collections import defaultdict

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = min(arr[i+1]-arr[i] for i in range(len(arr)-1))
        result = [[arr[i], arr[i+1]] for i in range(len(arr)-1) if arr[i+1]-arr[i] == min_diff]
        return result
MOD = 10**9 + 7

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        numbers = dict()
        arr.sort()
        result = 0
        for root in range(len(arr)):
            numbers[arr[root]] = 1
            for left in range(root):
                if arr[root] % arr[left] == 0:
                    right = arr[root] // arr[left]
                    if right in numbers:
                        numbers[arr[root]] += numbers[arr[left]] * numbers[right]
                        numbers[arr[root]] %= MOD
        return sum(numbers.values()) % MOD
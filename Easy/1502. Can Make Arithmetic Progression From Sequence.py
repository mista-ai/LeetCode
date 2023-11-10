class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        count, current, apnum = 0, 0, arr[1] - arr[0]

        for i in range(len(arr)-1):
            current = apnum + arr[i]
            if current == arr[i+1]:
                count = count + 1

        if count+1 == len(arr):
            return True
        else:
            return False
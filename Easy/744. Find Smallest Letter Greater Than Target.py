# class Solution:
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         if letters[-1] <= target:
#             return letters[0]
#         start = 0
#         end = len(letters) - 1
#         while start <= end:
#             mid = (start + end) // 2
#             if letters[mid] > target:
#                 end = mid - 1
#             else:
#                 start = mid + 1
#         return letters[start]

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target and letters[mid - 1] <= target:
                return letters[mid]
            elif letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[0]
# from functools import cmp_to_key
#
#
# class Solution:
#     def bigger_first(self, a, b):
#         bin_a = bin(a)[2:].count('1')
#         bin_b = bin(b)[2:].count('1')
#         if bin_a > bin_b:
#             return 1
#         elif bin_a < bin_b:
#             return -1
#         else:
#             if a > b:
#                 return 1
#             elif a < b:
#                 return -1
#             else:
#                 return 0
#
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         return sorted(arr, key=cmp_to_key(self.bigger_first))

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x)[2:].count("1"), x))
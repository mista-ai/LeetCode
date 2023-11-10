# class Solution:
#     def findEvenNumbers(self, digits: List[int]) -> List[int]:
#         res = []
#         dic = Counter(digits)
#         for num in range(100,1000,2):
#             flag = 0
#             for i,j in Counter(str(num)).items():
#                 if dic[int(i)] < j:
#                     flag = 1
#             if flag == 0:
#                 res.append(num)
#         return res

from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        c = Counter(digits)

        return [
            i * 100 + j * 10 + k
            for i in range(1, 10)
            for j in range(0, 10)
            for k in range(0, 10, 2)
            if c[i] > 0 and c[j] > (i == j) and c[k] > (k == i) + (k == j)
        ]

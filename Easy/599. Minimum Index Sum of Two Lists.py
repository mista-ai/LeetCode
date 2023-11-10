class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {x:i for i,x in enumerate(list1)}
        sol = []
        min_index = len(list1)+len(list2)
        for i,x in enumerate(list2):
            if x in dic:
                if i + dic[x] < min_index:
                    min_index = i + dic[x]
                    sol = [x]
                elif i + dic[x] == min_index:
                    sol.append(x)
        return sol
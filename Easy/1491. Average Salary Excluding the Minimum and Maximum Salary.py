class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salar2 = salary[1:-1]
        return sum(salar2)/len(salar2)
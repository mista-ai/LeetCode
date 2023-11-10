class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = set(range(1, n + 1))
        trusting = set(map(lambda x: x[0], trust))
        possible = people - trusting
        trusting = set()
        if len(possible) == 1:
            possible = possible.pop()
            for x in trust:
                if x[0] not in trusting and possible == x[1]:
                    trusting.add(x[0])
            if len(trusting) == n - 1:
                return possible
            else:
                return -1
        return -1
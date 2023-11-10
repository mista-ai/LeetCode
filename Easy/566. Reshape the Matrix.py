class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c or len(mat) == r and len(mat[0]) == c:
            return mat
        result = list()
        curr = 0
        result.append([])
        for i in mat:
            for x in i:
                result[-1].append(x)
                curr += 1
                if curr == c:
                    result.append([])
                    curr = 0
        if result[-1] == []:
            result.pop()
        return result
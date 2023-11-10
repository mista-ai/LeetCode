class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def upgrade(array):
            result = [1]
            for i in range(1, len(array)):
                result.append(array[i] + array[i - 1])
            result.append(1)
            return result

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        row = 2
        ans = [[1], [1, 1]]
        while row < numRows:
            ans.append(upgrade(ans[-1]))
            row += 1
        return ans
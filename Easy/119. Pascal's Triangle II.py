class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def upgrade(array):
            result = [1]
            for i in range(1, len(array)):
                result.append(array[i] + array[i - 1])
            result.append(1)
            return result

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        row = 1
        ans = [1, 1]
        while row < rowIndex:
            ans = upgrade(ans)
            row += 1
        return ans
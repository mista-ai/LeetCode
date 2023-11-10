class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(area ** 0.5)
        while width > 0:
            a = area % width
            if a == 0:
                lenth = area // width
                return [lenth, width]
            width -= 1
        return [area, 1]
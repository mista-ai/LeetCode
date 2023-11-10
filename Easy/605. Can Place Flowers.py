class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plots = len(flowerbed)
        if plots == 1:
            return True if flowerbed[0] == 0 and n <= 1 or flowerbed[0] == 1 and n == 0  else False
        counter = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            counter += 1
        if plots > 2 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            counter += 1
        start = 2
        end = plots - 2
        while start < end:
            if flowerbed[start] == 0:
                if flowerbed[start + 1] == 1:
                    start += 3
                    continue
                if flowerbed[start - 1] == 1:
                    start += 1
                    continue
                else:
                    counter += 1
                    start += 2
                    continue
            else:
                if flowerbed[start + 1] == 1:
                    start += 3
                    continue
                else:
                    start += 2
        return counter >= n
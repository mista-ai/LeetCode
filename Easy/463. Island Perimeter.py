class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        perimeter = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    if j == 0 or (j > 0 and grid[i][j - 1] == 0):
                        perimeter += 1
                    if j == width - 1 or (j < width - 1 and grid[i][j + 1] == 0):
                        perimeter += 1
                    if i == 0 or (i > 0 and grid[i - 1][j] == 0):
                        perimeter += 1
                    if i == height - 1 or (i < height - 1 and grid[i + 1][j] == 0):
                        perimeter += 1
        return perimeter
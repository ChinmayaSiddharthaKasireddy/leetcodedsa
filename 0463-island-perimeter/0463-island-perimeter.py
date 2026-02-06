class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    
                    # Check up
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 1
                    # Check down
                    if i < rows - 1 and grid[i + 1][j] == 1:
                        perimeter -= 1
                    # Check left
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 1
                    # Check right
                    if j < cols - 1 and grid[i][j + 1] == 1:
                        perimeter -= 1
        
        return perimeter

        
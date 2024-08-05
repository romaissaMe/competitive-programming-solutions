class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        up = {x: set([2, 3, 4]) for x in [2, 5, 6]}
        down = {x: set([2, 5, 6]) for x in [2, 3, 4]}
        left = {x: set([1, 4, 6]) for x in [1, 3, 5]}
        right = {x: set([1, 3, 5]) for x in [1, 4, 6]}
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(cell, visited):
            if cell == (m - 1, n - 1):
                return True

            visited.add(cell)
            i, j = cell

            for r, c, direction in [(i + 1, j, down), (i - 1, j, up), (i, j + 1, right), (i, j - 1, left)]:
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited and grid[i][j] in direction and grid[r][c] in direction[grid[i][j]]:
                    if dfs((r, c), visited):
                        return True
            
            return False
        
        return dfs((0, 0), set())
        
      
        
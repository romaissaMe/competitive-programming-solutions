class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        memo={}

        def solve(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            if i== row-1 and j == col-1:
                return grid[row-1][col-1]
            
            if i>row-1 or j>col-1:
                return float('inf')

            ans = grid[i][j] + min(solve(i+1,j),solve(i,j+1))

            memo[(i,j)] = ans
            return ans
        
        ans = solve(0,0)
        return ans
        
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row,col = len(matrix),len(matrix[0])
        memo={}

        def solve(i,j):

            if i==row-1 and j<col:
                return matrix[i][j]
            
            if i>row-1 or j>col-1:
                return float('inf')
            
            res = matrix[i][j]+min(solve(i+1,j),solve(i+1,j-1),solve(i+1,j+1))
            
            memo[(i,j)]=res

            return res

        ans = min(solve(0,j) for j in range(col))
        return ans
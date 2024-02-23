class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sums = []
        
        for i in range(len(grid)-2):
            for j in range(0,len(grid[0])-2):
                hourglass = sum(grid[i][j:j+3])+grid[i+1][j+1]+sum(grid[i+2][j:j+3])
                sums.append(hourglass)
        return max(sums)
        
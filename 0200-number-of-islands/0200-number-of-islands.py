class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        ans=0
        m,n=len(grid),len(grid[0])

        def dfs(i,j,visited):

            visited.add((i,j))

            directions=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for di,dj in directions:
                if 0 <= di <m and 0 <= dj <n and grid[di][dj]=="1" and (di,dj) not in visited:
                    dfs(di,dj,visited)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j,visited)
                    ans+=1
        
        return ans

       
           



        
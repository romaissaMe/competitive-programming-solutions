from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = Queue()
        visited=set()
        m=len(grid)
        n=len(grid[0])
        ans,fresh=0,0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.put((i,j))
                if grid[i][j]==1:
                    fresh+=1

        while not q.empty() and fresh>0:
            for _ in range(q.qsize()):
                orange=q.get()
                i,j=orange

                for dx,dy in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=dx<m and 0<= dy<n and grid[dx][dy]==1:
                        grid[dx][dy]=2
                        q.put((dx,dy))
                        fresh-=1
            ans+=1

        if fresh==0:
            return ans
        else:
            return -1
    
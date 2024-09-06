from queue import Queue
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = Queue()
        m,n = len(maze),len(maze[0])

        visited=set()
        
        q.put((entrance[0],entrance[1],0))
        visited.add((entrance[0],entrance[1]))

        while not q.empty():

            i,j,level = q.get()
            
       
            if maze[i][j] == "." and level !=0 and (j == n-1 or j==0 or i == m-1 or i==0):
                return level
            
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ndx,ndy= i+dx,j+dy
                    if 0<=ndx<m and 0<=ndy<n and maze[ndx][ndy]=='.':
                        if (ndx,ndy) not in visited:
                            q.put((ndx,ndy,level+1))
                            visited.add((ndx,ndy))
                        

        return -1
        
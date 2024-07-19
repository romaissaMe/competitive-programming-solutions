from queue import Queue

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set()
        q = Queue()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.put((i, j))
                    visited.add((i, j))
                    break
            if not q.empty():
                break

        while not q.empty():
            i, j = q.get()
            ans = 4
            if i + 1 < rows:
                if grid[i + 1][j] == 1:
                    ans -= 1
                    if (i + 1, j) not in visited:
                        visited.add((i + 1, j))
                        q.put((i + 1, j))
            if i - 1 >= 0:
                if grid[i - 1][j] == 1:
                    ans -= 1
                    if (i - 1, j) not in visited:
                        visited.add((i - 1, j))
                        q.put((i - 1, j))
            if j + 1 < cols:
                if grid[i][j + 1] == 1:
                    ans -= 1
                    if (i, j + 1) not in visited:
                        visited.add((i, j + 1))
                        q.put((i, j + 1))
            if j - 1 >= 0:
                if grid[i][j - 1] == 1:
                    ans -= 1
                    if (i, j - 1) not in visited:
                        visited.add((i, j - 1))
                        q.put((i, j - 1))
            res += ans

        return res

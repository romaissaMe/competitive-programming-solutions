class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m,n = len(board),len(board[0])
        
        if board[click[0]][click[1]] =="M":
            board[click[0]][click[1]] ="X"
            return board
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def dfs(i,j,visited):
            
            visited.add((i,j))

            if board[i][j]!="E":
                return 
            
            mines=0
            for (r,c) in directions:
                if 0<=i+r<m and 0<=j+c<n and board[i+r][j+c] == "M":
                    mines+=1

            if mines>0:
                board[i][j] = str(mines)
            else:
                board[i][j] = "B"   
                for (r,c) in directions:
                    if 0<=i+r<m and 0<=j+c<n and (i+r,j+c) not in visited:
                        dfs(i+r,j+c,visited)
               


        dfs(click[0],click[1],set())
        return board
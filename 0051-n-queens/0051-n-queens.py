class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        usedCols = set()
        posDiag=set()
        negDiag=set()

    
        def backtrack(i,sol):

            nonlocal ans

            if i==n:
                ans.append(sol)
                return

            for j in range(n):
                if j not in usedCols and (i-j) not in negDiag and (i+j) not in posDiag:
                        sol[i]=j
                        usedCols.add(j)
                        negDiag.add(i-j)
                        posDiag.add(i+j)
                        backtrack(i+1,sol[::])
                        sol[i]=-1
                        usedCols.remove(j)
                        negDiag.remove(i-j)
                        posDiag.remove(i+j)


            return 
        
        def transformSolutions(solutions, n):
            transformed = []
            for solution in solutions:
                board = []
                for i in range(n):
                    row = ['.'] * n  
                    row[solution[i]] = 'Q'  
                    board.append(''.join(row)) 
                transformed.append(board)
            return transformed
        
        backtrack(0,[-1]*n)

        return transformSolutions(ans, n)

                    

        
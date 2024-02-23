class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        matrix = [ list(row) for row in strs]
        answer = 0
        for j in range(len(matrix[0])):
            column = [row[j] for row in matrix]
            for x in range(len(column)-1):
                if column[x]>column[x+1]:
                    answer +=1
                    break
                    
        return answer
        
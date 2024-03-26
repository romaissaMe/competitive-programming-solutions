class NumMatrix(object):
        def __init__(self, matrix):
            """
            :type matrix: List[List[int]]
            """
            self.matrix = matrix
            m, n = len(matrix), len(matrix[0])
            self.acc_matrix = [[0] * n for _ in range(m)]
            self.acc_matrix[0][0] = matrix[0][0]
            for j in range(1, n):
                self.acc_matrix[0][j] = self.acc_matrix[0][j - 1] + matrix[0][j]
            for i in range(1, m):
                self.acc_matrix[i][0] = self.acc_matrix[i - 1][0] + matrix[i][0]
            for i in range(1, m):
                for j in range(1, n):
                    self.acc_matrix[i][j] = self.acc_matrix[i - 1][j] + self.acc_matrix[i][j - 1] - self.acc_matrix[i - 1][j - 1] + matrix[i][j]

        def sumRegion(self, row1, col1, row2, col2):
            """
            :type row1: int
            :type col1: int
            :type row2: int
            :type col2: int
            :rtype: int
            """
            res = self.acc_matrix[row2][col2]
            if col1 > 0:
                res -= self.acc_matrix[row2][col1 - 1]
            if row1 > 0:
                res -= self.acc_matrix[row1 - 1][col2]
            if col1 > 0 and row1 > 0:
                res += self.acc_matrix[row1 - 1][col1 - 1]
            return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
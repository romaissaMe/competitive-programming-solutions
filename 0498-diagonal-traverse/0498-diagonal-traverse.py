class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        if not mat:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        dic = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                dic[i + j].append(mat[i][j])
        
        for key in sorted(dic.keys()):
            diag = dic[key]
            if key % 2 == 0:
                diag.reverse()
            result.extend(diag)
           
        return result

        
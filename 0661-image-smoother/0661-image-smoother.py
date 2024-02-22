class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        cells = [(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1),(0,1),(0,-1)]
        result = [[0 for x in range(len(img[0]))] for _ in range(len(img))]
        for r in range(len(img)):
            for c in range(len(img[0])):
                avg = img[r][c]
                n_c = 1
                for nei in cells:
                    x = r + nei[0]
                    y = c + nei[1]
                    if 0<= x < len(img) and 0<= y < len(img[0]):
                        avg+= img[x][y]
                        n_c+=1
                result[r][c] = avg/n_c
        
        return result



                

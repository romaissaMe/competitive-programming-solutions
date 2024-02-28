class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = "".join(map(str,digits))
        number = int(n)+1
        result = [int(x) for i in range(len(str(number))) for x in str(number)[i]]
        return result
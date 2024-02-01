class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 1 <= n <= 150:
            return n if n % 2 == 0 else n*2
        else:
            print("n must be between 0 and 150")
            return

        
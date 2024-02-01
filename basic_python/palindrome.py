class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if -2**31 <= x <= 2**31 - 1:
            value = str(x)
            size = len(value)
            for i in range(size//2):
                if value[i] != value[size-1-i]:
                    return False
            return True
        print('check the number range constraint')
        return 
        
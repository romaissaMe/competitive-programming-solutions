class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 0 <= n <= 5 * 10**6:
            if n <= 2:
                return 0
            primes = [True] * (n)
            primes[0], primes[1] = False, False
            p = 2
            while p * p <= n:
                if primes[p] == True:
                    for i in range(p * p, n, p):
                        primes[i] = False
                p += 1

            result = sum (1 for i in range(2, n ) if primes[i])
            return result

        print('check the input range constraints')
        return
        
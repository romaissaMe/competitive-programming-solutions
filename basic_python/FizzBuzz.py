class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer=[]
        if 1<=n<=10**4:
            for i in range(1,n+1):
                if i%3 == 0:
                    if i%5 == 0:
                       answer.append("FizzBuzz")
                    else:
                        answer.append("Fizz")
                elif i%5 == 0:
                    answer.append("Buzz")
                else:
                    answer.append(str(i))
        return answer        


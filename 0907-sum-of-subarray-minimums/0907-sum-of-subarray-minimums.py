from collections import deque
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        l=n*[-1]
        r=n*[n]
        stack=[]

        for i in range(n):
            while len(stack)>0 and arr[stack[-1]]>=arr[i]:
                stack.pop()

            if len(stack)>0:
                l[i] = stack[-1]
            stack.append(i)

        #now smaller elements from right
        stack=[]

        for i in range(n-1,-1,-1):
            while len(stack)>0 and arr[stack[-1]]>arr[i]:
                stack.pop()

            if len(stack)>0:
                r[i] = stack[-1]
            stack.append(i)

        mod = 10**9 + 7  

        # Calculate the sum of all minimum subarray values with their respective frequencies
        res = sum((i - l[i]) * (r[i] - i) * value for i, value in enumerate(arr)) % mod
        return res

        
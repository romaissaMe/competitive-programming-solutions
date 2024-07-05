from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trust_cp = defaultdict(int)

        for x in trust:
            trust_cp[x[0]]-=1
            trust_cp[x[1]]+=1

        
        for i in range(1, n + 1):
            if trust_cp[i] == n - 1:
                return i

        return -1

      
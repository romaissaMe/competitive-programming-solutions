from collections import defaultdict
from queue import Queue
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        courses=defaultdict(int)
        ans=[]
        for c,p in prerequisites:
            graph[p].append(c)
            courses[c]+=1
        
        q = Queue()

        for c in range(numCourses):
            if courses[c]==0:
                q.put(c)
        
        while not q.empty():
            p = q.get()
            ans.append(p)
            for c in graph[p]:
                courses[c]-=1
                if courses[c]==0:
                    q.put(c)
        if len(ans)==numCourses:
            return ans
        else: return []





        


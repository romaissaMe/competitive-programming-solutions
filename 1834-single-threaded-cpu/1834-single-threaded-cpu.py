import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        li = []
        res=[]
        idx_tasks=[(task[0], task[1], i) for i, task in enumerate(tasks)]
        idx_tasks.sort()
        t=0
        n = len(tasks)
        i=0

        while len(res)<n:
            while i <n and idx_tasks[i][0] <= t:  
                heapq.heappush(li,(idx_tasks[i][1], idx_tasks[i][2]))
                i+=1

            if li:   
                proc_time,index=heapq.heappop(li)
                t+=proc_time
                res.append(index)
            else:
                if i < n:
                    t = idx_tasks[i][0]

        return res


            
        
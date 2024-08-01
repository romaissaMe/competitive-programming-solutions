from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq=Counter(s)
        heap=[[-cnt,char] for char,cnt in freq.items()]
        heapq.heapify(heap)
        ans=""
        prev = None

        while heap or prev:
            if prev and not heap:
                return ""
                
            cnt, char = heapq.heappop(heap)
            ans+=char
            cnt+=1

            if prev:
                heapq.heappush(heap,prev)
                prev = None

            if cnt !=0:
                prev=[cnt,char]
        
        return ans


       

        
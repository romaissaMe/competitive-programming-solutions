from queue import Queue
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q=Queue()
        q.put(0)
        graph={i:rooms[i] for i in range(len(rooms))}
        visited=set()
        
        while not q.empty():
            c = q.get()
            if c not in visited:
                visited.add(c)
                for next_room in graph[c]:
                    q.put(next_room)


        return len(visited) == len(rooms)
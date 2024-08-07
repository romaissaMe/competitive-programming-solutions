import heapq
from collections import defaultdict
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms_used = []  # (end_time, room_number)
        available_rooms=[i for i in range(n)]
        rooms_count = defaultdict(int)
        
        meetings.sort(key=lambda x: x[0])
        heapq.heapify(available_rooms)

        for i in range(len(meetings)):
            s, e = meetings[i]
            while rooms_used and rooms_used[0][0]<=s:
                _, room = heapq.heappop(rooms_used)
                heapq.heappush(available_rooms,room)
            
            if available_rooms:
                room= heapq.heappop(available_rooms)
                heapq.heappush(rooms_used,(e,room))
                rooms_count[room]+=1

            else:
                end_time, room = heapq.heappop(rooms_used)
                new_end_time = end_time + (e - s)
                heapq.heappush(rooms_used,(new_end_time,room))
                rooms_count[room] += 1
        
        max_meetings = max(rooms_count.values())
        return min(room for room, cnt in rooms_count.items() if cnt == max_meetings)

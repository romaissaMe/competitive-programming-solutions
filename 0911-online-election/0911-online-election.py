from collections import defaultdict,Counter
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons=persons
        self.times=times
        self.leader_at_times=defaultdict(int)
        
        current_leader = -1
        vote_count=defaultdict(int)
        for person, time in zip(persons, times):
            vote_count[person] += 1
            if current_leader == -1 or vote_count[person] >= vote_count[current_leader]:
                if current_leader != person:
                    current_leader = person
                self.leader_at_times[time]= current_leader


    def q(self, t: int) -> int:
        low=0
        high=len(self.times)-1
        while low<=high:
            mid=(low+high)//2
            if t == self.times[mid]:
                return self.leader_at_times[t]
            if t<self.times[mid]:
                high=mid-1
            else:
             low = mid+1

        return self.leader_at_times[self.times[high]]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
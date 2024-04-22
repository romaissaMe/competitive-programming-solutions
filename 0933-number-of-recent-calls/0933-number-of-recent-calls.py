from queue import Queue
class RecentCounter:

    def __init__(self):
        self.ctp = Queue()
        

    def ping(self, t: int) -> int:
        self.ctp.put(t)
        while self.ctp.queue[0]<t-3000:
            self.ctp.get()
        return self.ctp.qsize()
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
from queue import Queue
class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k =k
        self.q=Queue()

    def consec(self, num: int) -> bool:
        self.q.put(num)
        if self.q.qsize()<self.k:
            return False
        else:
            if self.q.qsize()>self.k:
                self.q.get()
            for i in range(self.k):
                if self.q.queue[i-1] != self.value:
                    return False
            return True
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
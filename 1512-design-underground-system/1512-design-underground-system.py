class UndergroundSystem(object):

    def __init__(self):
        self.checkins= {}
        self.systemMap={}


    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkins[id] = [stationName,t]
        return None
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, t_start = self.checkins[id]
        if (startStation,stationName) in self.systemMap:
            self.systemMap[(startStation,stationName)][0]+=abs(t-t_start)
            self.systemMap[(startStation,stationName)][1]+=1
        else:
            self.systemMap[(startStation,stationName)]=[abs(t-t_start),1]
        return None

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        time, count = self.systemMap[(startStation,endStation)]
        return time/float(count)



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
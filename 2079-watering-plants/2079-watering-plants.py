class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps=0
        CAP = capacity
        for i,p in enumerate(plants):
            if p <= capacity:
                capacity-=p
                steps+=1
            else:
               capacity =  CAP
               steps+= 2*i+1    
               capacity-=p
        return steps
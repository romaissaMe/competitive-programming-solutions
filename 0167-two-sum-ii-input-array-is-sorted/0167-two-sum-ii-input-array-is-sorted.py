class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        #find the boundary
        h = len(numbers)-1
        l = 0
    

        while l < h:
            i = (l + h) // 2  
            if numbers[i] > target:
                h = i  
            else:
                l = i + 1 
        
        h=l
        l=0
        while l<h:
            if numbers[l]+numbers[h]>target:
                h-=1
            elif numbers[l]+numbers[h]==target:
                return [l+1,h+1]
            else:
                l+=1
        


                
        
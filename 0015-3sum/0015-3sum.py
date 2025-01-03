class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        ans = []
        for i in range(0,len(nums)):
            
            if i>0 and nums[i]==nums[i-1]:
                continue

            l=i+1 
            h=len(nums)-1
            while l<h:
                sum_= nums[l] + nums[h] + nums[i]
                if sum_<0 :
                    l+=1
                     
                if sum_>0:
                    h-=1
                
                if sum_==0:
                    ans.append([nums[i],nums[l],nums[h]])
                    l+=1
                    while nums[l] == nums[l-1] and l<h: 
                        l+=1
            
        return ans




            



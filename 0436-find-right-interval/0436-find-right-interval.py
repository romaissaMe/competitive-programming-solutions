class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        dic = {val[0]:idx for idx,val in enumerate(intervals)}
        sorted_st = sorted(dic.keys())
        _max=sorted_st[-1]
        ans=[]

        for interval in intervals:
            low,high=0,len(sorted_st)-1
            res=-1
            while low<=high:
                mid = (low+high)//2
                if sorted_st[mid]>=interval[1]:
                    res=mid
                    high=mid-1
                else:
                    low=mid+1
            
           
            if res!=-1:
                ans.append(dic[sorted_st[res]])
            else: ans.append(-1)
            
        return ans
 


        
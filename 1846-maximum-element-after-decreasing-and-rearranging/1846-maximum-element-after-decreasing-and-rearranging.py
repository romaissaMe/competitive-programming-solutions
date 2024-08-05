class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)

        sorted_arr[0]=1
        max_ = 1

        for i in range(1,len(arr)):
            sorted_arr[i]=min(sorted_arr[i-1]+1,sorted_arr[i])
            max_ = max(max_,sorted_arr[i])
        
        return max_
        
        
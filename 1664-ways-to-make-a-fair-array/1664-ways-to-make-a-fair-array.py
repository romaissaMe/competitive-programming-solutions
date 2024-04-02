class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pref_sum = [0]*n
        sum_odd=0
        sum_even=0
        res = 0
        last_odd,last_even = [n-1,n-2] if n%2 ==0 else [n-2,n-1]
        
        for i,x in enumerate(nums):
            if i %2 ==0:
                sum_even+=x
                pref_sum[i]=sum_even
            else:
                sum_odd +=x
                pref_sum[i]=sum_odd
      
        for i,x in enumerate(nums):
            tmp = 0  if i-1<0 else pref_sum[i-1]

            if i%2 == 0:
                new_even =  pref_sum[i]-x + pref_sum[last_odd]-tmp
                new_odd = tmp+ pref_sum[last_even]-pref_sum[i]
            else:
                new_even =tmp+ pref_sum[last_odd]-pref_sum[i] 
                new_odd = pref_sum[i]-x + pref_sum[last_even]-tmp
            if new_even == new_odd :
                res+=1


        return res



        # [6,1,7,4,1]
        # 0,1,2,3,4
        # [6,7,4,1]
        #  0,1,2,3,4
        #   odd                  odd [1,4]
        #                    even 6 7 1
        # [6,1,7,4,1]      
        # 0,1,2,3,4
        # [6,1,4,1]  odd 1 1       1 = last_pref_even - pref i
        #  0,1,2,3   even 6 4   4 = las_pref_odd - pref_odd_judt bef i
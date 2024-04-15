class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = [int(char) for char in str(num) if char.isdigit()]
        if num>0:
            nums=sorted(nums)
            if nums[0]==0:
                for i in range(len(nums)):
                    if nums[i] != 0 :
                        nums[0],nums[i]=nums[i],nums[0]
                        break
        else:
            nums = sorted(nums,reverse=True)  

        answer = int("".join(map(str,nums)))
        return answer if num>0 else answer*(-1)
        
                
        
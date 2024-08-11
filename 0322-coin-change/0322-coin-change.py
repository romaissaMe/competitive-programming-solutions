class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}

        def solve(sumSub):
            if sumSub in memo:
                return memo[sumSub]

            if sumSub == 0:
                return 0
            
            if sumSub < 0:
                return float('inf')  

    
            
            remain_coins=float('inf')  
            for coin in coins:
                res= solve(sumSub - coin)
                if res != float('inf'):
                    remain_coins=min(remain_coins,res+1)                 
            
            memo[sumSub]=remain_coins
            return remain_coins

        
        ans=solve(amount)
        return ans if ans != float('inf') else -1
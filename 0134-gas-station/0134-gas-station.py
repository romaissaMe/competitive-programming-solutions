class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
    
        if total_gas < total_cost:
            return -1
        
        st_index = 0
        current_gas = 0
        
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                st_index = i + 1
                current_gas = 0
        
        return st_index
        
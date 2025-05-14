class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = 0
        totalCost = 0
        curr_gas = 0
        start_idx = 0
        
        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                start_idx = (i+1)%len(gas)
                curr_gas = 0
        
        if totalGas < totalCost:
            return -1
        return start_idx
        

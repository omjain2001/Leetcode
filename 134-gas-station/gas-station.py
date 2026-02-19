class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if not gas or not cost:
            return -1

        start_index = 0
        count = 0
        curr_gas = 0

        for i in range(len(gas)):
            curr_gas = curr_gas + gas[i] - cost[i]
            if curr_gas < 0:
                curr_gas = 0
                start_index = (i+1)%len(gas)
        
        curr_gas = 0
        count = len(gas)
        while(count):
            curr_gas = curr_gas + gas[start_index] - cost[start_index]
            if curr_gas < 0:
                return -1
            count -= 1
            start_index = (start_index + 1) % len(gas)
        return start_index       
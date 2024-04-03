class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalCost = 0, totalGas = 0, starting_point = 0, curr_gas = 0;
        for(int i=0; i<gas.size(); i++){
            totalCost += cost[i];
            totalGas += gas[i];
            curr_gas += gas[i] - cost[i];
            if(curr_gas < 0){
                starting_point = i+1;
                curr_gas = 0;
            }
        }
        return totalGas >= totalCost ? starting_point : -1;
    }
};
class Solution {
public:
    bool isPossible(vector<int>& nums) {
        map<int,int> freq, need;
        for(auto ele: nums){
            freq[ele]++;
            need[ele] = 0;
        }

        for(auto ele: nums){
            if(freq[ele] == 0) continue;
            if(need[ele] > 0){
                need[ele]--;
                freq[ele]--;
                need[ele+1]++;
            } else if(freq[ele] > 0 && freq[ele+1] > 0 && freq[ele+2] > 0){
                freq[ele]--;
                freq[ele+1]--;
                freq[ele+2]--;
                need[ele+3]++;
            } else return false;
        }
        return true;
    }
};
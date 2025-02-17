class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        map<int,int> m;
        for(int i=0; i<position.size(); i++){
            m[-position[i]] = speed[i];
        }
        int res = 0; double cur = 0;
        for(auto ele: m){
            double time = (double)(target+ele.first)/ele.second;
            if(time > cur){
                res++;
                cur = time;
            }
        }

        return res;
    }
};
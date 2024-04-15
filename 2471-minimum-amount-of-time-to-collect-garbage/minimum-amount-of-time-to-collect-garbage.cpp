class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int time = 0;
        int n = garbage.size();
        vector<int> cum(n,0);
        for(int i=0; i<travel.size(); i++){
            cum[i+1] = cum[i] + travel[i];
        }

        int mc = 0, mi = 0, pc = 0, pi = 0, gc = 0, gi = 0;

        for(int i = n-1; i>=0; i--){
            for(auto j: garbage[i]){
                if(j == 'M'){
                    mc++;
                    if(mi == 0) mi = i;
                } else if(j == 'P'){
                    pc++;
                    if(pi == 0) pi = i;
                } else {
                    gc++;
                    if(gi == 0) gi = i;
                }
            }
        }

        time = cum[mi] + cum[pi] + cum[gi] + mc + gc + pc;

        return time;
    }
};
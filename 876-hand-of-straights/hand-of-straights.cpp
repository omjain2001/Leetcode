class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if(hand.size() % groupSize != 0) return false;
        sort(hand.begin(),hand.end());
        map<int,int> res, need;
        for(auto ele: hand){
            res[ele]++;
            need[ele] = 0;
        }
        for(int i=0; i<hand.size(); i++){
            if(res[hand[i]] == 0 && need[hand[i]] > 0) return false;
            else if(need[hand[i]] == 0 && res[hand[i]] > 0){
                for(int j=hand[i]; j<hand[i]+groupSize; j++){
                    if(res.find(j) == res.end() || res[j] == 0) return false;
                    res[j]--;
                }
            } else {
                res[hand[i]]--;
                need[hand[i]]--;
            }
        }

        return true;
    }
};
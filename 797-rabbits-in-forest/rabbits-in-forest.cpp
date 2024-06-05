class Solution {
public:
    int numRabbits(vector<int>& answers) {
        sort(answers.begin(), answers.end());
        int ans = 0;
        for(int i=0; i<answers.size(); i++){
            ans += (answers[i] + 1);
            int count = answers[i];
            int j = i+1;
            while(j < answers.size() && answers[j] == answers[i] && count){
                j++;
                count--;
            }
            i = j-1;
        }
        return ans;
    }
};
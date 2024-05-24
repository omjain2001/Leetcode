class Solution {
public:
    int recur(vector<string> &words, map<char,int> &m, vector<int> &score, int i){
        if(i >= words.size()) return 0;
        int take = 0;
        bool valid = true;
        map<char,int> temp;
        for(auto ele: words[i]){
            temp[ele]++;
            if(m[ele] < temp[ele]){
                valid = false;
                break;
            }
        }
        if(valid){
            for(auto ele: words[i]){
                m[ele]--;
                take += score[ele-'a'];
            }
            take += recur(words,m,score,i+1);
            for(auto ele: words[i]){
                m[ele]++;
            }
        }
        return max(take, recur(words,m,score,i+1));
    }
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        map<char,int> m;
        for(auto ele: letters) m[ele]++;
        return recur(words,m,score,0);
    }
};
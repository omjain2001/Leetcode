class Solution {
public:
    bool recur(vector<vector<char>> &board, vector<vector<int>> &visitor, map<int,vector<pair<int,int>>> &m, int i, int x, int y, string word){
        if(i == word.size()) return true;
        vector<pair<int,int>> cor = m[word[i]];
        for(int j=0; j<cor.size(); j++){
            if(visitor[cor[j].first][cor[j].second] == 0){
                if((x < 0 && y < 0) || abs(cor[j].first-x) + abs(cor[j].second-y) == 1){
                    visitor[cor[j].first][cor[j].second] = 1;
                    if(recur(board,visitor,m,i+1,cor[j].first,cor[j].second,word)) return true;
                    visitor[cor[j].first][cor[j].second] = 0;
                }
            }
        }
        return false;
        
    }
    bool exist(vector<vector<char>>& board, string word) {
        vector<vector<int>> visitor(board.size(), vector<int>(board[0].size(), 0)) ;
        map<int,vector<pair<int,int>>> m;

        for(int i=0; i<board.size(); i++){
            for(int j=0; j<board[0].size(); j++){
                m[board[i][j]].push_back({i,j});
            }
        }

        // for (auto ele: m){
        //     for (auto i: ele){
        //         cout<<i.first<<" "<<i.second<<endl;
        //     }
        //     cout<<endl;
        // }
        return recur(board,visitor,m,0,-1,-1, word);
    }
};
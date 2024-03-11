class Solution {
public:
    bool rowValidation(vector<vector<char>> &board){
        for(int i=0; i<board.size(); i++){
            set<char> s;
            int count = 0;
            for(int j=0; j<board[i].size(); j++){
                if(board[i][j] != '.'){
                    count++;
                    s.insert(board[i][j]);
                }
            }
            if(s.size() != count) return false;
        }
        return true;
    }
    bool colValidation(vector<vector<char>> &board){
        for(int i=0; i<board[0].size(); i++){
            set<char> s;
            int count = 0;
            for(int j=0; j<board.size(); j++){
                if(board[j][i] != '.'){
                    count++;
                    s.insert(board[j][i]);
                }
            }
            // cout<<s.size()<<" -> "<< count<<" === ";
            if(s.size() != count) return false;
        }
        // cout<<endl;
        return true;
    }
    bool blockValidation(vector<vector<char>> &board){
        for(int i=0; i<board.size(); i+=3){
            for(int j=0; j<board[0].size(); j+=3){
                set<char> s;
                int count = 0;
                for(int k=i; k<i+3; k++){
                    for(int l=j; l<j+3; l++){
                        if(board[k][l] != '.'){
                            s.insert(board[k][l]);
                            count++;
                        }
                    }
                }
                if(count != s.size()) return false;
            }
        }
        return true;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        bool ans = true;
        ans = rowValidation(board);
        ans &= colValidation(board);
        ans &= blockValidation(board);
        return ans;
    }
};
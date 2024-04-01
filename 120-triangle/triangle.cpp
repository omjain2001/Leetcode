class Solution {
public:
    int recur(vector<vector<int>>& triangle, int i, int r, vector<vector<int>> &arr){
        if(r >= triangle.size() || i >= triangle[r].size()) return 0;
        if(arr[i][r] != -1) return arr[i][r];
        int op1 = triangle[r][i] + recur(triangle, i, r+1, arr);
        int op2 = triangle[r][i] + recur(triangle, i+1, r+1, arr);
        return arr[i][r] = min(op1,op2);
    }
    int minimumTotal(vector<vector<int>>& triangle) {
        // priority_queue<int, vector<int>, greater<int>> pq;
        // int sum = 0;
        // for(int i=0; i<triangle.size(); i++){
        //     for(int j=0; j<triangle[i].size(); j++){
        //         pq.push(triangle[i][j]);
        //     }
        //     sum += pq.top();
        //     pq.pop();
        //     while(!pq.empty()) pq.pop();
        // }
        int r = triangle.size();
        vector<vector<int>> arr(triangle[r-1].size(), vector<int>(r, -1));
        return recur(triangle, 0, 0, arr);
    };
};
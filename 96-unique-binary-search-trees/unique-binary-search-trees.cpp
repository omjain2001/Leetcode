class Solution {
public:
    long long dp[50][50];
    int combinations(int st, int e){
        if(st > e) return 1;
        if(st == e) return 1;
        if(dp[st][e] != -1) return dp[st][e];
        int sum = 0;
        for(int i=st; i<=e; i++){
            int leftCom = dp[st][i-1] = combinations(st,i-1);
            int rightCom = dp[i+1][e] = combinations(i+1,e);
            sum += (leftCom * rightCom);
        }
        return dp[st][e] = sum;
    }
    int numTrees(int n) {
        for(int i=0; i<20; i++){
            for(int j=0; j<20; j++){
                dp[i][j] = -1;
            }
        }
        return combinations(1,n);
    }
};
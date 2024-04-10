class Solution {
public:
    int recur(int n, int i, int t[]){
        if(i == n || i == n+1) return 1;
        if(i > n+1) return 0;
        if(t[i-1] != -1) return t[i-1];
        return t[i-1] = recur(n,i+1,t) + recur(n,i+2,t);        
    }
    int climbStairs(int n) {
        int t[n+1];
        memset(t,-1, (n+1) * sizeof(int));
        // return recur(n,1,t);
        t[n] = 1;
        t[n-1] = 1;
        for(int i=n-2; i>=0; i--){
            t[i] = t[i+1] + t[i+2];
        }
        return t[0];
    }
};
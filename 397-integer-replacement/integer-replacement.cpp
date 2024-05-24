class Solution {
public:
    long long recur(long long n){
        if(n == 1) return 0;
        if(n % 2 == 0) return 1 + recur(n/2);
        else {
            return 1 + min(recur(n-1),recur(n+1));
        }
    }
    int integerReplacement(int n) {
        // int count = 0;
        // while(n != 1){
        //     if(n % 2 == 0) n /= 2;
        //     else n = n-1;
        //     count++;
        // }
        // return count;
        return recur(n);
    }
};
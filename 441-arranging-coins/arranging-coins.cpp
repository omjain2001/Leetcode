class Solution {
public:
    int arrangeCoins(int n) {
        long long l = 1, r = n;
        long long sum = 0;
        while(sum <= n){
            sum = (l * (l+1))/2;
            if(sum <= n) r = l;
            ++l;
        }
        return r;
    }
};
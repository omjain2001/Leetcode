class Solution {
public:
    int mySqrt(int x) {
        long long int l = 1, r = x;
        while(l <= r){
            long long int mid = (l+r)/2;
            if((mid*mid) == x) return mid;
            else if((mid*mid) > x) r = mid-1;
            else l = mid+1;
        }
        return r;
    }
};
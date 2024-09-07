class Solution {
public:
    bool isPerfectSquare(int num) {
        long long int l = 1, r = num;
        while(l <= r){
            long long int mid = (l+r)/2;
            if((mid*mid) == num) return true;
            else if((mid*mid) > num) r = mid-1;
            else l = mid+1;
        }
        return false;
    }
};
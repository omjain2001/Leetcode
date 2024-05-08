class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> v(1,1);
        int x = 0, y = 0, z = 0;
        while(v.size() < n){
            int minimum = min({2 * v[x], 3 * v[y], 5 * v[z]});
            v.push_back(minimum);
            if(minimum == 2 * v[x]) x++;
            if(minimum == 3 * v[y]) y++;
            if(minimum == 5 * v[z]) z++;
        }
        return v[n-1];
    }
};
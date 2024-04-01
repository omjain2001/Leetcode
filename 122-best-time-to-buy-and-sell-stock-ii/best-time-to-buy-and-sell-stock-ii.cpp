class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxi = 0;
        int cp = prices[0];
        for(int i=1; i<prices.size(); i++){
            if(prices[i] > cp){
                maxi = maxi + (prices[i] - cp);
            }
            cp = prices[i];
        }
        return maxi;
    }
};
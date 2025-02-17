class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        
        int n = heights.size();
        stack<int> s;
        
        // // Solution 1 - Computing PSE (previous smaller element) and NSE (Next smaller element)
        // vector<int> pse(n,-1);
        // vector<int> nse(n,n);

        // // Compute PSE
        // for(int i=0; i<n; i++){
        //     while(!s.empty() && heights[s.top()] >= heights[i]) s.pop();
        //     if(s.empty()) pse[i] = -1;
        //     else pse[i] = s.top();
        //     s.push(i);
        // }

        // // Clear the stack
        // while(!s.empty()) s.pop();

        // // Compute NSE
        // for(int i=n-1; i>=0; i--){
        //     while(!s.empty() && heights[s.top()] >= heights[i]) s.pop();
        //     if(s.empty()) nse[i] = n;
        //     else nse[i] = s.top();
        //     s.push(i);
        // }

        // // Compute max area
        // int maxi = INT_MIN;
        // for(int i=0; i<n; i++){
        //     maxi = max(maxi, heights[i]*(nse[i]-pse[i]-1));
        // }


        // Solution 2 - Without using two vectors

        int maxi = INT_MIN;
        vector<int> pse(n,-1);
        
        for(int i=0; i<n; i++){
            while(!s.empty() && heights[s.top()] >= heights[i]){
                maxi = max(maxi, heights[s.top()] * (i - pse[s.top()] - 1));
                s.pop();
            }
            if(s.empty()) pse[i] = -1;
            else pse[i] = s.top();
            s.push(i);
        }

        while(!s.empty()){
            maxi = max(maxi, heights[s.top()] * (n - pse[s.top()] - 1));
            s.pop();
        }

        return maxi;
    }
};
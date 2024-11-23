class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        // sort(fruits.begin(), fruits.end());
        int b1=-1, b2=-1, c1=0, c2=0;
        int ans = 0;
        int j = 0;
        for(int i=0; i<fruits.size(); i++){
            if(b1 == -1 || b1 == fruits[i]){
                b1 = fruits[i];
                c1++;
            } else if(b2 == -1 || b2 == fruits[i]){
                b2 = fruits[i];
                c2++;
            }
            else {
                while(j < i && c1 > 0 && c2 > 0){
                    if(b1 == fruits[j]) c1--;
                    else c2--;
                    j++;
                }
                if(c1 == 0){
                    b1 = fruits[i];
                    c1++;
                }
                if(c2 == 0){
                    b2 = fruits[i];
                    c2++;
                }
            }
            ans = max(ans, c1+c2);
        }
        return ans;
    }
};
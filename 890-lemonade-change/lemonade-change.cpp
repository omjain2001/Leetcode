class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int f=0, ten=0, twn=0;
        for(int i=0; i<bills.size(); i++){
            if(bills[i] == 5) f++;
            else if(bills[i] == 10){
                if(f > 0){
                    f--;
                    ten++;
                } else return false;
            } else {
                if(f > 0 && ten > 0){
                    f--;
                    ten--;
                    twn++;
                } else if(f >= 3) {
                    f-=3;
                    twn++;
                } else return false;
            }
        }
        return true;
    }
};
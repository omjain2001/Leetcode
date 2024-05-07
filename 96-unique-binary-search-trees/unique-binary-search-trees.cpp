class Solution {
public:
    int combinations(int st, int e){
        if(st > e) return 1;
        if(st == e) return 1;
        int sum = 0;
        for(int i=st; i<=e; i++){
            int leftCom = combinations(st,i-1);
            int rightCom = combinations(i+1,e);
            sum += (leftCom * rightCom);
        }
        return sum;
    }
    int numTrees(int n) {
        return combinations(1,n);
    }
};
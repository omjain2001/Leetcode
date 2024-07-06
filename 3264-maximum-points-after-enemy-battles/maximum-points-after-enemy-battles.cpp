class Solution {
public:
    long long maximumPoints(vector<int>& enemyEnergies, int currentEnergy) {
        sort(enemyEnergies.begin(), enemyEnergies.end());
        long long left = 0, right = enemyEnergies.size()-1;
        long long points = 0;
        while(left <= right){
            if(currentEnergy >= enemyEnergies[left]){
                points += currentEnergy/enemyEnergies[0];
                currentEnergy %= enemyEnergies[left];
            } else if(points > 0) {
                currentEnergy += enemyEnergies[right];
                right--;
            } else return 0;
        }
        return points;
    }
};
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> arr(26,0);
        for(auto ele: tasks) arr[ele-'A']++;
        sort(arr.begin(), arr.end());
        int chunk = arr[25] - 1;
        int count = chunk * n;
        for(int i=24; i>=0; i--){
            count -= min(chunk,arr[i]);
        }

        if(count < 0) return tasks.size();
        return tasks.size() + count;
    }
};
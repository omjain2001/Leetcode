class TimeMap {
public:
    // unordered_map<string, vector<pair<int, string>>> m;
    map<string, map<int,string>> m;
    TimeMap() {

    }
    
    void set(string key, string value, int timestamp) {
        this->m[key][timestamp] = value;
    }
    
    string get(string key, int timestamp) {
        // vector<int> v;
        // for(auto ele: m[key]) v.push_back(ele.first);
        // vector<int>::iterator itr;
        // itr = lower_bound(v.begin(), v.end(), timestamp);
        auto itr = m[key].upper_bound(timestamp);
        if(itr == m[key].begin()) return "";
        else return prev(itr)->second;
        // int n = v.size();
        // int l = 0, r = n-1;
        // while(l <= r){
        //     int mid = (l+r)/2;
        //     if(v[mid] == timestamp) return m[key][v[mid]];
        //     else if(v[mid] < timestamp) l = mid+1;
        //     else r = mid-1;
        // }
        // if(r == -1) return "";
        // return m[key][v[r]];
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
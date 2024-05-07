class Solution {
public:
    string addBinary(string a, string b) {
        int carry = 0;
        string ans = "";
        int i = a.length()-1, j  = b.length()-1;
        while(i >= 0 && j >= 0){
            int cnt = 0;
            // string ai = (string)a[i];
            // string bj = b[j];
            ans = to_string(((int)a[i] - 48) ^ ((int)b[j] - 48) ^ carry) + ans;
            if(((int)a[i] - 48) == 1) cnt++;
            if(((int)b[j] - 48) == 1) cnt++;
            if(carry == 1) cnt++;
            if(cnt > 1) carry = 1;
            else carry = 0;
            i--;
            j--;
        }

        while(i >= 0){
            ans = to_string(((int)a[i] - 48) ^ carry) + ans;
            carry = ((int)a[i] - 48) & carry;
            i--;
        }

        while(j >= 0){
            ans = to_string(((int)b[j] - 48) ^ carry) + ans;
            carry = ((int)b[j] - 48) & carry;
            j--;
        }

        if(carry) ans = "1" + ans;

        return ans;
    }
};
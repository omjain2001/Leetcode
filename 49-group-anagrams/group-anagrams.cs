public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {

        // Clarifications
        // 1. Are the strings in the list in lowercase?
        // 2. Any constraint on size of the list?
        // It is given that the final order does not matter

        // Approaches
        // 1. Create a copy of the list, sort each element, and map the similar strings to their corresponding original strings (TC: O(nlgm), SC: O(n) + O(number of unique anagrams))
        // 2. For each string, find the unique representation of it. Store this representation as the key and the original string as an element of the list as its value. (TC: O(k) where k is the total length of all strings), SC: O(number of unique anagrams))

        Dictionary<string, List<string>> m = new Dictionary<string, List<string>>();
        foreach(string str in strs){
            string anagram = findAnagram(str);
            if (m.ContainsKey(anagram)){
                m[anagram].Add(str);
            } else {
                m.Add(anagram, new List<string>{str});
            }
        }

        IList<IList<string>> ans = new List<IList<string>>();

        foreach (KeyValuePair<string,List<string>> ele in m){
            ans.Add(ele.Value);
        }

        return ans;
        
    }

    string findAnagram(string s){
        // Declare a list of size 26 (representing the lowercase alphabets)
        int[] chars = new int[26];

        // Compute the count of the letters in the given s
        foreach(char ch in s){
            int idx = (int)ch - (int)'a';
            chars[idx] += 1;
        }

        // Concat the letters in the unique way that will uniquely identify this anagram
        string result = "";
        for (int i=0; i<26; i++){
            if (chars[i] > 0){
                result += chars[i];
                result += (char)(i + (int)'a');
            }
        }

        return result;

    }
}
public class Solution {
    public bool IsAnagram(string s, string t) {
        
        // Clarifications:
        // Two empty strings are anagram of each other
        // All the input letters are lowercase letters
        
        // Approaches:
        // Option 1: Sort both the strings and check the equality => TC O(nlgn), SC O(1)
        // Option 2: Maintain the count of letters in both the words using hashmap and check the equality
        // Option 3: If all of them are ascii characters, we will maintain an array of 26 letters (in case of only lowercase letters) or 128 characters to accommodate all of them

        // Define a function to count the letters in the word and derive their representation

        if (GetAnagramRepresentation(s) == GetAnagramRepresentation(t)) return true;
        return false;

    }

    string GetAnagramRepresentation(string word){
        int[] chars = new int[26];

        foreach (char ch in word){
            int idx = (int) ch - (int)'a';
            chars[idx] += 1;
        }

        string ans = "";

        // Generate unique representation of the character count
        for (int i=0; i<26; i++){
            if (chars[i] > 0){
                ans += (char)(chars[i] + '0');
                ans += (char)(i+(int)'a');
            }
        }

        return ans;
    }
}
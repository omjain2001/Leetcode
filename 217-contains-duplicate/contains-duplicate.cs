public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        
        // Find the duplicate element in an array

        // Option 1: Sort the array and iterate to check if next element in same as current element
        // Option 2: Maintain the count of the elements in hashmap. If the count is greater than 1,
        // that element is duplicated
        // Option 3: Since we just want to know if that element has occurred before and not to maintain the count,
        // we can use the hashset to store distinct elements.

        // Let's implement Option 3
        HashSet<int> s = new HashSet<int>();
        foreach (int ele in nums){
            if (s.Contains(ele)) return true;
            s.Add(ele);
        }
        
        return false;
    }
}
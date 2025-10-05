public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
        // Clarifications
        // Any contraints on number of elements?
        // Nature of elements (postive + negative)?
        // Can duplicate numbers be present in an array?

        // Approaches
        // Option 1: For every element, I will check all the subsequent elements in an array to see if
        // (target-nums[i]) is present. If yes, return [i,j]. If not, repeat for next element
        // TC: O(n^2), SC: O(1)

        // Option 2: Make a pair of (element, index), sort the array in ascending order based on elements,
        // Use two pointers to get the two elements

        int[][] sorted_arr = new int[nums.Length][];

        for (int i=0; i<nums.Length; i++){
            sorted_arr[i] = new int[] {nums[i],i};
        }

        Array.Sort(sorted_arr, (a,b) => a[0].CompareTo(b[0]));

        int l=0, r=nums.Length-1;
        while(l < r){
            int sum = sorted_arr[l][0] + sorted_arr[r][0];
            if (sum == target) return [sorted_arr[l][1], sorted_arr[r][1]];
            else if(sum > target) r -= 1;
            else l += 1;
        }

        return new int[]{-1,-1};
         
    }
}
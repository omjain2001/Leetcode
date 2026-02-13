import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Brute force
        # Create new array and add all elements in sorted order and find median

        # Better approach
        # Use binary search to partition array such that all elements left 
        # to the partition are the elements left to the median

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)

        INT_MIN = -1e10
        INT_MAX = 1e10

        left = (n1+n2+1) // 2

        l, r = 0, n1
        while(l <= r):

            mid = (l+r) // 2
            l1 = l2 = INT_MIN
            r1 = r2 = INT_MAX

            rem = left - mid

            l1 = nums1[mid-1] if (mid-1) >= 0 else INT_MIN
            l2 = nums2[rem-1] if (rem-1) >= 0 else INT_MIN
            r1 = nums1[mid] if mid < n1 else INT_MAX
            r2 = nums2[rem] if rem < n2 else INT_MAX

            if l1 <= r2 and l2 <= r1:
                if (n1+n2)%2 == 0:
                    return (max(l1,l2) + min(r1,r2)) / 2
                return max(l1,l2)
            elif l1 > r2:
                r = mid - 1
            else:
                l = mid + 1
        
        return 0 
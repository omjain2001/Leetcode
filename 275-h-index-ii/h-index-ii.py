class Solution:
    def hIndex(self, citations: List[int]) -> int:

        '''
        Intuition: This problem is similar to the koko banana problem. We have to find the maximum h such that the 
        researcher has published atleast h papers and each one has atleast h citations

        Also, we have been given that the citations is sorted. So somewhere we can think of applying binary search
        algorithm. 

        What will be the range of h? min = 0, max = len(citations)

        Brute force - 
        For every h in this range, we can iterate through the citations and check the condition. 
        Time complexity will be O(n^2)

        Better solution - 
        Instead of sequential iteration, we can use binary search to find the value of h
        Time complexity will be O(nlgn)
        '''

        def check_h_index(h):
            count = 0
            for ele in citations:
                if ele >= h:
                    count += 1
            return count >= h

        # Min and Max value of h
        l = 0 # empty array
        r = len(citations) # all citations are greater than equal to number of papers published

        # Binary search
        while(l <= r):
            mid = (l+r)//2
            if (check_h_index(mid)):
                l = mid + 1
            else:
                r = mid - 1
        
        return r
    


        
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        start_loc = [[ele[1],ele[0]] for ele in trips]
        end_loc = [[ele[2],ele[0]] for ele in trips]

        start_loc.sort()
        end_loc.sort()

        end = 0
        i = 0
        count = 0
        while(i < len(trips)):
            if start_loc[i][0] < end_loc[end][0]:
                count += start_loc[i][1]
                i += 1
            else:
                count -= end_loc[end][1]
                end += 1
            
            if count > capacity:
                return False
        
        return True
            
        
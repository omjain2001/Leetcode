class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = triplets.copy()
        temp = []
        for i in range(3):
            valid = False
            for t in curr:
                if t[i] <= target[i]:
                    temp.append(t)
                if t[i] == target[i]:
                    valid = True
            if not valid:
                return False
            curr = temp.copy()
            temp = []
        
        result = [0,0,0]
        for t in curr:
            result[0] = max(result[0], t[0])
            result[1] = max(result[1], t[1])
            result[2] = max(result[2], t[2])
        
        return (result == target)
                

        
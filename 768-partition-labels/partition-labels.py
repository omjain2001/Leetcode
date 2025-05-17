class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 0:
            return []
        end_idx = [-1 for i in range(26)]
        idx = 0
        for ch in s:
            end_idx[ord(ch)-ord('a')] = idx
            idx += 1
        
        ranges = []
        idx = 0
        for ch in s:
            if end_idx[ord(ch)-ord('a')] >= 0:
                ranges.append([idx, end_idx[ord(ch)-ord('a')]])
                end_idx[ord(ch)-ord('a')] = -1
            idx += 1
        
        ranges.sort(key=lambda x: [x[0],x[1]])

        # Merge intersecting ranges
        ans = []
        start = ranges[0][0]
        end = ranges[0][1]

        for ele in ranges[1:]:
            if start <= ele[0] <= end:
                end = max(end, ele[1])
            else:
                ans.append(end-start+1)
                start = ele[0]
                end = ele[1]
        
        ans.append(end-start+1)
        return ans


        


        
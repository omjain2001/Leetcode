class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []

        rs = 0
        re = len(matrix)-1
        cs = 0
        ce = len(matrix[0])-1

        ans = []

        while(rs <= re and cs <= ce):

            # Right
            if rs <= re:
                for j in range(cs, ce+1):
                    ans.append(matrix[rs][j])
                rs += 1
            
            if cs <= ce:
                for i in range(rs, re+1):
                    ans.append(matrix[i][ce])
                ce -= 1
            

            # Left
            if rs <= re:
                for j in range(ce, cs-1, -1):
                    ans.append(matrix[re][j])
                re -= 1
                
            

            # Top
            if cs <= ce:
                for i in range(re, rs-1, -1):
                    ans.append(matrix[i][cs])
                cs += 1
        
        return ans


        
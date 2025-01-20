class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows=len(mat) 
        cols=len(mat[0])
        mat_pos={}
        for r in range(rows) : 
            for c in range(cols) : 
                mat_pos[mat[r][c]]=(r,c) 
        row=[0]*rows 
        col=[0]*cols 
        for i in range(len(arr)) : 
            r,c=mat_pos[arr[i]]
            row[r]+=1 
            col[c]+=1 
            if row[r]==cols or col[c]==rows : 
                return i
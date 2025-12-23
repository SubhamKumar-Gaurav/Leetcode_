class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n=len(mat)
        arr=[]  
        for i in range(n) : 
            arr.append([mat[i].count(1), i]) 
        
        arr.sort(key=lambda x: (x[0], x[1])) 

        res=[] 
        for i in range(k) : 
            res.append(arr[i][1]) 
        
        return res 
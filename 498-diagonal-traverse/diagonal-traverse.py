from collections import defaultdict 

class Solution: 
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]: 
        n=len(mat) 
        m=len(mat[0]) 
        d=defaultdict(list) 
        for i in range(n) : 
            for j in range(m) : 
                d[i+j].append(mat[i][j]) 
        res=[] 
        for i in d : 
            if i%2==0 : 
                for j in reversed(d[i]) : 
                    res.append(j) 
            else : 
                for j in d[i] : 
                    res.append(j) 
        return res 
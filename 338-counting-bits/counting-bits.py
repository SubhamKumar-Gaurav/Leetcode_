class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1) : 
            b=bin(i)[2:] 
            res.append(b.count("1")) 
        return res 
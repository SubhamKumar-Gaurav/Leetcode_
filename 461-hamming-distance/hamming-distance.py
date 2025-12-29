class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res=0 
        bx=bin(x)[2:] 
        by=bin(y)[2:] 
        if len(bx)>len(by) : 
            by="0"*(len(bx)-len(by))+by 
        else : 
            bx="0"*(len(by)-len(bx))+bx 

        for i in range(len(by)) : 
            if by[i]!=bx[i] : 
                res+=1 
        return res 
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        res=[]
        for i in range(n) :  
            temp1=set(A[:i+1]) 
            temp2=set(B[:i+1]) 
            ans=temp1.intersection(temp2) 
            res.append(len(ans)) 
        return res 
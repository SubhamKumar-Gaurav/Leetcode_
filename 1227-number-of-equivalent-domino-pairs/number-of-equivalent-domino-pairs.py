from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int: 
        new=[]
        for i in dominoes :  
            temp1=min(i)
            temp2=max(i) 
            new.append(tuple((temp1, temp2))) 

        d=defaultdict(int) 
        for i in new :  
            d[i]+=1 
             
        ans=0 
        for i in d : 
            if d[i]>1 : 
                n=d[i]-1 
                ans+=(n*(n+1))//2
        return ans
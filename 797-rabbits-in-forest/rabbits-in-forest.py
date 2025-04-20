import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c=0 
        d={} 
        for i in answers : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]=1 

        for i in d :  
            c+=math.ceil(float(d[i])/(i+1))*(i+1)
        return c
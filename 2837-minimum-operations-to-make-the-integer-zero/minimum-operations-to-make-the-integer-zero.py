class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int: 
        for t in range(1, 61) :  
            val=num1-(t*num2) 
            b=bin(val)[2:] 
            if val>0 :
                if b.count("1")<=t<=val : 
                    return t
            else : 
                break 
        return -1 
from collections import defaultdict, Counter 
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n&(n-1)==0 : 
            return True 
        d=defaultdict(dict)
        for i in range(31) : 
            temp=2**i
            s=str(temp)
            c=Counter(s)
            sorted_c=sorted(c.items())
            d[i]=sorted_c 
        s=str(n) 
        c=Counter(s) 
        sorted_c=sorted(c.items())
        for i in d :
            if sorted_c == d[i] : 
                return True 
        return False 
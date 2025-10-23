class Solution:
    def hasSameDigits(self, s: str) -> bool:
        l=[] 
        for i in s : 
            l.append(int(i)) 

        while len(l)>2 : 
            for i in range(len(l)-1) : 
                l[i]=(l[i]+l[i+1])%10 
            l.pop() 
        return l[0]==l[1]
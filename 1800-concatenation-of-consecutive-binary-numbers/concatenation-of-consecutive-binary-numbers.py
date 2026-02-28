class Solution:
    def concatenatedBinary(self, n: int) -> int: 
        MOD=1000000007
        s="" 
        for i in range(1, n+1) : 
            b=bin(i)[2:] 
            s+=b 
            if int(s)>=MOD : 
                temp=int(s, 2)%MOD 
                s=bin(temp)[2:] 
        return int(s, 2)%MOD 
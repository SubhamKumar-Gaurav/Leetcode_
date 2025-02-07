class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def dig_sum(n) : 
            c=0 
            while n>0 : 
                c+=n%10 
                n=n//10
            return c 
        d=defaultdict(int) 
        for i in range(lowLimit, highLimit+1) : 
            temp=dig_sum(i) 
            d[temp]+=1  
        res=1
        for i in d : 
            res=max(res, d[i])
        return res 
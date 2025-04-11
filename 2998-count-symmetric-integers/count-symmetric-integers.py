class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int: 
        def dig_sum(n) : 
            ans=0 
            while n>0 : 
                ans+=(n%10) 
                n=n//10 
            return ans

        def sym_sum(s) : 
            a=int(s[:len(s)//2])
            b=int(s[len(s)//2:]) 
            return dig_sum(a)==dig_sum(b)             
        count=0 
        for i in range(low, high+1) : 
            s=str(i) 
            if len(s)%2==0 :  
                if sym_sum(s) : 
                    count+=1 
        return count
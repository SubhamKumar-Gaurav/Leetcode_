class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool: 
        def gcd(a,b) : 
            if b==0 : 
                return a 
            return gcd(b, a%b) 

        d={} 
        for i in deck : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]=1 
        count_arr=[] 
        for i in d : 
            count_arr.append(d[i])

        gcd_val=count_arr[0]  
        for i in range(1, len(count_arr)) : 
            gcd_val=gcd(gcd_val, count_arr[i]) 
            
        return gcd_val>=2
class Solution: 
    def bestClosingTime(self, customers: str) -> int: 
        n=len(customers) 
        prefix=[0]*n     # Stores count of "N"
        if customers[0]=="N" : 
            prefix[0]=1 
        
        for i in range(1, n) : 
            prefix[i]=prefix[i-1]
            if customers[i]=="N" : 
                prefix[i]+=1  
        prefix.insert(0,0) 
        
        suffix=[0]*n     # Stores count of "Y"
        if customers[-1]=="Y" : 
            suffix[-1]=1 
        
        for i in range(n-2, -1, -1) :  
            suffix[i]=suffix[i+1] 
            if customers[i]=="Y" : 
                suffix[i]+=1 
        suffix.append(0)  

        penalty=[] 
        for i in range(n+1) : 
            penalty.append( suffix[i]+prefix[i] ) 

        minPenalty=min(penalty) 
        for i in range(n+1) : 
            if penalty[i]==minPenalty : 
                return i 

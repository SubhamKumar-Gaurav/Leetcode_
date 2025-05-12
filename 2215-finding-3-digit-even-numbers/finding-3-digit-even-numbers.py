class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]: 
        n=len(digits)
        ans=[] 
        for i in range(n) :  
            a=str(digits[i]) 
            for j in range(n) : 
                if i!=j : 
                    b=str(digits[j]) 
                    for k in range(n) : 
                        if j!=k and i!=k :          
                            c=str(digits[k]) 
                            if digits[k]%2==0 : 
                                temp=a+b+c
                                if int(temp)>99 : 
                                    ans.append(int(temp)) 
        res=set(ans) 
        ans=[] 
        for i in res : 
            ans.append(i) 
        ans.sort() 
        return ans 
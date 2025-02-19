class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def gen_str(n, chars=["a", "b", "c"]) : 
            if n==0 : 
                return [""] 
            smaller_str=gen_str(n-1, chars)
            res=[] 
            for s in smaller_str : 
                for c in chars : 
                    res.append(s+c) 
            return res 

        def happy_str(res) :  
            for j in range(len(res)-1) :
                if res[j]==res[j+1]  : 
                    return False 
            return True 
        
        chars=["a", "b", "c"]
        res=gen_str(n, chars) 
        ans=[]
        for i in range(len(res)) : 
            if happy_str(res[i]) : 
                ans.append(res[i]) 
        ans.sort() 
        if k>len(ans) : 
            return "" 
        return ans[k-1]
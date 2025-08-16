class Solution:
    def numberOfWays(self, n: int, x: int) -> int: 
        def dfs(i, remain) : 
            nonlocal n, kMod

            # base case
            if remain==0 :   
                return 1 

            # if remain reaches negative or i**x is more than remain
            if remain<0 or pow(i,x)>remain :  
                return 0 
            
            # already present in memo 
            if (i, remain) in memo : 
                return memo[(i, remain)] 
            
            skip=dfs(i+1, remain) 
            new_remain=remain-pow(i,x) 
            pick=dfs(i+1, new_remain) 
            memo[(i, remain)] = (skip+pick) % kMod 
            return memo[(i, remain)] 

        kMod = 10**9 + 7 
        memo=dict() 
        return dfs(1, n)
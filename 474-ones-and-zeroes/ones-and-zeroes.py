
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int: 
        dp={} 

        def dfs(i, m, n) : 
            if i==len(strs) : 
                return 0 
            if (i, m, n) in dp : 
                return dp[(i, m, n)] 
            
            zero=strs[i].count("0") 
            one=strs[i].count("1")
            dp[(i, m, n)] = dfs(i+1, m, n) 
            if zero<=m and one<=n : 
                dp[(i, m, n)] = max(dfs(i, m, n), 1+dfs(i+1, m-zero, n-one))        
            return dp[(i, m, n)]
        return dfs(0, m, n) 
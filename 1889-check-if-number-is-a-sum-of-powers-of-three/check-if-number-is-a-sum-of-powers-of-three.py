class Solution:
    def checkPowersOfThree(self, n: int) -> bool: 
        def backtrack(i, curr) : 
            if curr==n : 
                return True 
            if curr>n or 3**i>n : 
                return False 
            if backtrack(i+1, curr+3**i) : 
                return True 
            return backtrack(i+1, curr)  
        return backtrack(0, 0)
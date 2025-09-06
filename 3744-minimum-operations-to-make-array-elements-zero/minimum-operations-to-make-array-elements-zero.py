
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int: 
        def solve(l,r) : 
            steps=0 
            L=1 
            S=1 
            while L<=r : 
                R=(4*L)-1 
                start=max(L, l) 
                end=min(R, r) 
                if start<=end : 
                    steps+=(end-start+1)*S 
                S+=1 
                L*=4 
            return steps 

        ans=0 
        for l,r in queries : 
            steps=solve(l,r) 
            ans+=(steps+1)//2 
        return ans
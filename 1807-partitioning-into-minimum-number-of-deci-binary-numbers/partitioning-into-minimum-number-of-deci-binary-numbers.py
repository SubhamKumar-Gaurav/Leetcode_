class Solution:
    def minPartitions(self, n: str) -> int: 
        ans=int(n[0]) 
        for i in n : 
            ans=max(ans, int(i)) 
        return ans
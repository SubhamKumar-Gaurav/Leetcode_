class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n) : 
            s=str(n)[::-1] 
            return int(s) 
        
        return abs(n-reverse(n))
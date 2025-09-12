class Solution:
    def trap(self, height: List[int]) -> int: 
        n=len(height) 
        lmax=[0]*n 
        lmax[0]=height[0] 
        for i in range(1,n) : 
            lmax[i]=max(lmax[i-1], height[i]) 
        
        rmax=[0]*n 
        rmax[-1]=height[-1] 
        for i in range(n-2, -1, -1) : 
            rmax[i]=max(rmax[i+1], height[i]) 
        
        ans=0 
        for i in range(1, n-1) : 
            wall=min(lmax[i], rmax[i]) 
            ans+=max(0, wall-height[i]) 
        return ans
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums) 

        if n==1 : 
            return 0 
        
        ans=float("-inf")
        nums.sort()  
        for i in range(1, n) : 
            ans=max(ans, nums[i]-nums[i-1]) 
        
        return ans 
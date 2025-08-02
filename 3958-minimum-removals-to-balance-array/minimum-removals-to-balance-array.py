class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int: 
        n=len(nums) 
        if n==1 : 
            return 0 
        if n==2 : 
            if max(nums)<=k*min(nums) : 
                return 0 
            else : 
                return 1 
        nums.sort() 
        i=0 
        j=0 
        ans=float("inf")
        while j<n and i<n : 
            while j<n and i<n and nums[j]<=k*nums[i] : 
                ans=min(ans, n-(j-i+1)) 
                j+=1 
            i+=1 
        return ans 
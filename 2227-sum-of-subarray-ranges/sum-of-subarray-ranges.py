class Solution: 
    def subArrayRanges(self, nums: List[int]) -> int: 
        n=len(nums) 
        ans=0 
        for i in range(n-1) : 
            minVal=float("inf")  
            maxVal=float("-inf")
            minVal=min(minVal, nums[i])  
            maxVal=max(maxVal, nums[i])
            for j in range(i+1, n) : 
                minVal=min(minVal, nums[j])
                maxVal=max(maxVal, nums[j]) 
                ans+=(maxVal-minVal) 
        return ans 
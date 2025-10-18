class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort() 
        ans=float("-inf")  
        i=0 
        j=len(nums)-1 
        while i<j : 
            ans=max(ans, nums[i]+nums[j]) 
            i+=1 
            j-=1 
        return ans
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0 
        for i in range(n) : 
            ans=max(ans, abs(nums[i%n]-nums[(i+1)%n])) 
        return ans
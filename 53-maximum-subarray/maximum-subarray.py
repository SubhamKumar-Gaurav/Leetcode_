class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums) 
        res=nums[0]
        maxEnding=nums[0] 
        for i in range(1,n) : 
            maxEnding=max(maxEnding+nums[i], nums[i])
            res=max(res, maxEnding)
        return res 
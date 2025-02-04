class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=nums[0] 
        count=1 
        res=ans 
        for i in range(1,len(nums)) : 
            if nums[i]>nums[i-1] :  
                ans+=nums[i] 
                count+=1 
            else : 
                ans=nums[i] 
                count=1 
            res=max(res, ans) 
        return res 
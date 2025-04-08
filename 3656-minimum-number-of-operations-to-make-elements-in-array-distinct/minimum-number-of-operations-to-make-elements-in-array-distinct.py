class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0 
        while len(nums)!=len(set(nums)) : 
            if len(nums)>=3 : 
                del nums[0] 
                del nums[0]
                del nums[0]
                ans+=1  
            if len(nums)==2 : 
                if len(set(nums))!=2 : 
                    ans+=1 
                    break 
        return ans
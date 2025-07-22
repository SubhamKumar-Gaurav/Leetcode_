
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        d={} 
        res=nums[0] 
        curr=nums[0] 
        d[nums[0]]=1 
        i=0 
        j=1 
        while i<n-1 and j<n : 
            if nums[j] not in d : 
                curr+=nums[j] 
                res=max(res, curr) 
                d[nums[j]]=1 
                j+=1 
            else : 
                curr-=nums[i]
                del d[nums[i]]
                i+=1 
        return res
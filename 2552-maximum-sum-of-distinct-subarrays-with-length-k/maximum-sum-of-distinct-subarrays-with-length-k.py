from collections import defaultdict 

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int: 
        if len(set(nums))<k : 
            return 0 
        if len(set(nums))==k and len(nums)==k : 
            return sum(nums) 
        n=len(nums) 
        d=defaultdict(int) 
        l=0 
        maxSum=0 
        currSum=0 
        for r in range(n) : 
            d[nums[r]]+=1 
            currSum+=nums[r] 
            while len(d)>k or r-l+1>k: 
                d[nums[l]]-=1 
                currSum-=nums[l]  
                if d[nums[l]]==0 : 
                    del d[nums[l]] 
                l+=1
                if r-l+1==k and len(d)==k : 
                    maxSum=max(maxSum, currSum)
                
            if r-l+1==k and len(d)==k :  
                maxSum=max(maxSum, currSum)
        return maxSum 
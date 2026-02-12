from collections import defaultdict 

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n=len(nums) 
        ans=float("inf") 
        d={} 
        for i in range(n) : 
            if nums[i] in d : 
                ans=min(ans, i-d[nums[i]]) 
            rev=int(str(nums[i])[::-1]) 
            d[rev]=i 
        if ans==float("inf") : 
            return -1 
        return ans 
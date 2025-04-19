class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int: 
        nums.sort() 
        within_upper=0 
        l=0 
        r=len(nums)-1 
        while l<r :  
            if nums[l]+nums[r]>upper : 
                r-=1 
            else : 
                within_upper+=(r-l) 
                l+=1 
        l=0 
        r=len(nums)-1 
        below_lower=0 
        while l<r : 
            if nums[l]+nums[r]>=lower : 
                r-=1 
            else : 
                below_lower+=(r-l)
                l+=1 
        return within_upper-below_lower
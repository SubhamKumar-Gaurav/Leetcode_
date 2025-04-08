class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int: 
        n=len(nums)
        nums.sort() 
        l=[nums[0]]
        ans=0  
        for i in range(1,n) :  
            if nums[i]>l[-1] : 
                l.append(nums[i]) 
            else : 
                diff=l[-1]-nums[i]
                l.append(nums[i]+diff+1) 
                ans+=(diff+1) 
        return ans
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        n=len(nums) 
        nums.sort(reverse=True)
        c=n/3
        ans=0 
        for i in range(1, n, 2) : 
            if c>0 : 
                ans+=nums[i]
                c-=1
        return ans
       
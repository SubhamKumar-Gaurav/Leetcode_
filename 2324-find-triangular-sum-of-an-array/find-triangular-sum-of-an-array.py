class Solution:
    def triangularSum(self, nums: List[int]) -> int: 
        n=len(nums) 
        
        for i in range(n) : 
            for j in range(1, len(nums)) : 
                if len(nums)>1 : 
                    nums[j-1]=(nums[j-1]+nums[j])%10 
            if len(nums)>1 :
                nums.pop() 
        return nums[0] 
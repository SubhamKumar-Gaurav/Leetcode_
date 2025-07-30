class Solution:
    def longestSubarray(self, nums: List[int]) -> int: 
        n=len(nums)
        max_nums=max(nums) 
        c=0 
        temp=0 
        for i in range(n) :  
            if nums[i]==max_nums : 
                temp+=1 
            else : 
                temp=0 
            c=max(c, temp) 
        return c
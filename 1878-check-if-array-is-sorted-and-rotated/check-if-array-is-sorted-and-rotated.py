class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        k=0  
        for i in range(n-1) : 
            if nums[i]>nums[i+1] : 
                k+=1 
                j=i+1
        if k==0 : 
            return True 
        elif k>1 : 
            return False 
        else : 
            if (nums[j:]+nums[:j])==sorted(nums) : 
                return True 
            else : 
                return False
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1) : 
            if nums[i]==nums[i+1] : 
                nums[i]=nums[i]*2 
                nums[i+1]=0 
        zero_count=nums.count(0) 
        temp=[] 
        for i in range(len(nums)) : 
            if nums[i]!=0 : 
                temp.append(nums[i]) 
        for j in range(zero_count) :
            temp.append(0)
        return temp
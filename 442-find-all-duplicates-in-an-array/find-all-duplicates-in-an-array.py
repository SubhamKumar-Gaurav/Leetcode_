class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]: 
        n=len(nums)
        nums.sort() 
        arr=[] 
        for i in range(1, n) : 
            if nums[i-1]==nums[i] : 
                arr.append(nums[i]) 
        return arr 
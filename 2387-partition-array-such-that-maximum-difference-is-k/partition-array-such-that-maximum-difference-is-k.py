class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int: 
        nums.sort() 
        c=1 
        i=0 
        j=1 
        while i<j and i<len(nums) and j<len(nums) : 
            if abs(nums[i]-nums[j])>k : 
                c+=1 
                i=j 
            j+=1 
        return c 
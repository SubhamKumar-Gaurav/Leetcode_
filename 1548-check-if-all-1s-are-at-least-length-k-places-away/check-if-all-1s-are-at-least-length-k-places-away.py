class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n=len(nums) 
        prev=None 
        for i in range(len(nums)) : 
            if nums[i]==1 : 
                prev=i
                break 
        if prev is None : 
            return True

        for i in range(prev+1, n) : 
            if nums[i]==1 : 
                if (i-prev-1)<k : 
                    return False 
                prev=i 
        return True 
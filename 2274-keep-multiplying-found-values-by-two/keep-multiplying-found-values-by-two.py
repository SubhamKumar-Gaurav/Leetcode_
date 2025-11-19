class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums : 
            return original 
        
        n=len(nums)
        s=set(nums) 
        curr=original 
        while True : 
            curr=curr*2 
            if curr not in s : 
                return curr 
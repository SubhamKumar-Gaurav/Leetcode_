class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int: 
        n=len(nums)
        res=0 
        score=0 
        i=0 
        j=0 
        while j<n :  
            score+=nums[j] 
            while i<=j and score*(j-i+1)>=k : 
                score-=nums[i] 
                i+=1 
            res+=j-i+1
            j+=1 
        return res 
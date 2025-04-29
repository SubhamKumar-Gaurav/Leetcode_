class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)  
        max_val=max(nums)  
        i=0 
        ans=0 
        curr=0 
        for j in range(n) : 
            if nums[j]==max_val : 
                curr+=1 
            while curr>=k : 
                ans+=n-j 
                if nums[i]==max_val : 
                    curr-=1 
                i+=1 
        return ans 
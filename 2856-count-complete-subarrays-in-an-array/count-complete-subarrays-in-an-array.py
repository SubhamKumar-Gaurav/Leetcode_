class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        s=set(nums) 
        target=len(s)  
        c=0  
        for i in range(n) :  
            s=set()
            s.add(nums[i]) 
            if len(s)==target : 
                c+=1 
            for j in range(i+1,n) : 
                s.add(nums[j]) 
                if len(s)==target : 
                    c+=1 
        return c 
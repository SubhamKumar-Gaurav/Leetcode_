class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n=len(nums)  
        prefixArr=[0]*n 
        prefixArr[0]=1  
        temp=1  
        for i in range(1, n) : 
            if nums[i-1]<nums[i] : 
                temp+=1 
            else : 
                temp=1 
            prefixArr[i]=temp 
        
        temp=1 
        suffixArr=[0]*n 
        suffixArr[-1]=1 
        for i in range(n-2, -1, -1) : 
            if nums[i]<nums[i+1] : 
                temp+=1 
            else : 
                temp=1 
            suffixArr[i]=temp 
        
        ans=1 
        for i in range(1, n) : 
            ans=max(ans, min(prefixArr[i-1], suffixArr[i])) 
        
        return ans 
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n=len(nums)
        prefixSum=[0]*n 
        suffixSum=[0]*n 
        prefixSum[0]=nums[0] 
        for i in range(1,n) : 
            prefixSum[i]=prefixSum[i-1] 
            prefixSum[i]+=nums[i] 
        suffixSum[-1]=nums[-1] 
        for i in range(n-2,-1,-1) : 
            suffixSum[i]=suffixSum[i+1] 
            suffixSum[i]+=nums[i] 
        c=0 
        for i in range(n-1) : 
            diff=abs(prefixSum[i]-suffixSum[i+1]) 
            if diff%2==0 : 
                c+=1 
        return c    
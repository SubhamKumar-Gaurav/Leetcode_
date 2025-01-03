class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums) 
        prefixSum=[0]*n 
        suffixSum=[0]*n 
        prefixSum[0]=nums[0] 
        suffixSum[n-1]=nums[n-1] 
        for i in range(1,n) : 
            prefixSum[i]=prefixSum[i-1] 
            prefixSum[i]+=nums[i] 
        for i in range(n-2,-1,-1) : 
            suffixSum[i]=suffixSum[i+1] 
            suffixSum[i]+=nums[i]
        count=0  
        for i in range(n-1) : 
            if prefixSum[i]>=suffixSum[i+1] : 
                count+=1 
        return count
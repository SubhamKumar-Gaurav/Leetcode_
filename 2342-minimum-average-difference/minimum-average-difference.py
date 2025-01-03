class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)
        prefixSum=[0]*n 
        prefixSum[0]=nums[0]
        for i in range(1,n) : 
            prefixSum[i]=prefixSum[i-1] 
            prefixSum[i]+=nums[i] 
        suffixSum=[0]*(n+1) 
        suffixSum[n]=0 
        for i in range(n-1,-1,-1) : 
            suffixSum[i]=suffixSum[i+1] 
            suffixSum[i]+=nums[i]
        diff=[0]*n 
        minval=float("inf") 
        idx=0 
        for i in range(n) : 
            if (n-i-1)!=0 : 
                temp=abs(prefixSum[i]//(i+1)-suffixSum[i+1]//(n-i-1))
            else : 
                temp=abs(prefixSum[i]//(i+1))
            diff[i]=temp 
            if diff[i]<minval : 
                minval=diff[i]
                idx=i
        return idx
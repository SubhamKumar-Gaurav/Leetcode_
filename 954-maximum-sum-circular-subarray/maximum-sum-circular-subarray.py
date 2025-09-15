class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadanesAlgo(arr) : 
            n=len(arr) 
            maxEnding=arr[0] 
            res=arr[0] 
            for i in range(1, n) : 
                maxEnding=max(maxEnding+arr[i], arr[i]) 
                res=max(res, maxEnding) 
            return res 

        n=len(nums)
        maxSubarraySum=kadanesAlgo(nums) 
        if maxSubarraySum<0 : 
            return maxSubarraySum 
        totalArrSum=nums[0]
        nums[0]=-nums[0] 
        for i in range(1,n) : 
            totalArrSum+=nums[i] 
            nums[i]=-nums[i] 
        minSubarraySum=kadanesAlgo(nums) 
        maxCircularSubarraySum=totalArrSum+minSubarraySum 
        return max(maxCircularSubarraySum, maxSubarraySum)
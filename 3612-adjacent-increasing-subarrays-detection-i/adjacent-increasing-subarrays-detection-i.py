class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def isIncreasing(arr) : 
            n=len(arr) 
            for i in range(1,n) : 
                if arr[i-1]>=arr[i] : 
                    return False 
            return True 
        
        n=len(nums) 
        for i in range(n-(2*k)+1) : 
            j=i+k
            arr1=nums[i:j] 
            arr2=nums[j:j+k] 
            if isIncreasing(arr1) and isIncreasing(arr2) : 
                return True 
        return False 
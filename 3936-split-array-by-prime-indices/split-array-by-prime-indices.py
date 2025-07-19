class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n=len(nums) 
        if n==1 : 
            return sum(nums)
            
        arr=[True]*(n+1) 
        arr[0]=False 
        arr[1]=False 
        i=2 
        for i in range(2, int(n**0.5)+1) : 
            if arr[i] : 
                for j in range(i*i, n+1, i) : 
                    arr[j]=False                   
      
        sum_A=0 
        sum_B=0
        for i in range(len(nums)) : 
            if arr[i] : 
                sum_A+=nums[i] 
            else : 
                sum_B+=nums[i] 
        return abs(sum_A-sum_B) 
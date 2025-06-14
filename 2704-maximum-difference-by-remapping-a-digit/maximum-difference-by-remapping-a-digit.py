class Solution:
    def minMaxDifference(self, num: int) -> int:  
        first=0 
        nums=str(num)
        for i in nums : 
            if i!="9" : 
                first=i 
                break 
        arr1=list(nums) 
        arr2=list(nums)
        for i in range(len(arr1)) : 
            if arr1[i]==first : 
                arr1[i]="9" 
        max_val=int("".join(arr1)) 
        first=nums[0]
        for i in range(len(arr2)) : 
            if arr2[i]==first : 
                arr2[i]="0" 
        min_val=int("".join(arr2)) 
        return max_val-min_val
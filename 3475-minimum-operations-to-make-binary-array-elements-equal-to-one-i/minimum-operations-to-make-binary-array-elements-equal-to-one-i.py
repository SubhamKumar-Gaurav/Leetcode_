class Solution:
    def minOperations(self, nums: List[int]) -> int: 
        c=0 
        for i in range(len(nums)-2) : 
            if nums[i]==0 : 
                nums[i]=1 
                if nums[i+1]==0 : 
                    nums[i+1]=1 
                else : 
                    nums[i+1]=0 
                if nums[i+2]==0 : 
                    nums[i+2]=1 
                else : 
                    nums[i+2]=0 
                c+=1 
        if 0 in nums : 
            return -1 
        else : 
            return c 
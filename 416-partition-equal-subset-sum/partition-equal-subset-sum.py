
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 : 
            return False 
        dp=set() 
        dp.add(0) 
        target=sum(nums)//2 
        for i in range(len(nums)-1, -1, -1) : 
            tempDP=set() 
            for t in dp : 
                tempDP.add(t+nums[i]) 
                tempDP.add(t) 
            dp=tempDP 
        if target in dp : 
            return True 
        return False 
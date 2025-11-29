class Solution: 
    def minOperations(self, nums: List[int], k: int) -> int: 
        sumNums=sum(nums) 
        return sumNums%k 
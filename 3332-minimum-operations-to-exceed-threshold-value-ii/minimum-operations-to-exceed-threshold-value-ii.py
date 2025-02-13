import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int: 
        heapq.heapify(nums) 
        count=0 
        while nums[0]<k :  
            a=heapq.heappop(nums)
            b=heapq.heappop(nums) 
            heapq.heappush(nums, 2*min(a,b)+max(a,b)) 
            count+=1 
        return count
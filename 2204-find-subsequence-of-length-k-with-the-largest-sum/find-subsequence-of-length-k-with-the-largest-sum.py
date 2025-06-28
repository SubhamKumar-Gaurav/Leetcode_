import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq=[] 
        for i in range(len(nums)) : 
            heapq.heappush(pq, (-nums[i], i)) 
        s=set()  
        for i in range(k) : 
            s.add(heappop(pq)) 

        arr=[] 
        for i in range(len(nums)) : 
            if (-nums[i], i) in s and len(arr)<k : 
                arr.append(nums[i])
        return arr
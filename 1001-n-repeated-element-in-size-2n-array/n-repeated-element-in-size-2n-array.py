from collections import defaultdict  

class Solution: 
    def repeatedNTimes(self, nums: List[int]) -> int: 
        d=defaultdict(int) 
        for i in nums : 
            d[i]+=1 
        
        for i in d : 
            if d[i]==len(nums)//2 : 
                return i 
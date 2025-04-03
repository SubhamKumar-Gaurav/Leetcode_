class Solution: 
    def maximumTripletValue(self, nums: List[int]) -> int:  
        ans=0 
        curr_max=0 
        diff=0 
        for x in nums : 
            ans=max(ans, diff*x)
            diff=max(diff, curr_max-x) 
            curr_max=max(curr_max, x) 
        return ans
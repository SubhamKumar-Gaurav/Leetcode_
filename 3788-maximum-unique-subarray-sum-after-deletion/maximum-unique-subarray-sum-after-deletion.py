class Solution:
    def maxSum(self, nums: List[int]) -> int:
        all_neg=True 
        for i in nums : 
            if i>=0 : 
                all_neg=False 
        if all_neg : 
            return max(nums) 
        d={} 
        for i in nums : 
            if i in d : 
                d[i]+=1 
            else : 
                if i>0 : 
                    d[i]=1 
        ans=0 
        for i in d : 
            ans+=i 
        return ans
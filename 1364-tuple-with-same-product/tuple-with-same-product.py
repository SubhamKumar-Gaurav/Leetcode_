class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int: 
        ans=0 
        c=Counter() 
        for i in range(len(nums)) : 
            for j in range(i) : 
                prod=nums[i]*nums[j] 
                ans+=c[prod]*8 
                c[prod]+=1 
        return ans 
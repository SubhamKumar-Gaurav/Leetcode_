class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def bSearch(nums,l,r,x) : 
            while l<=r : 
                mid=(l+r)//2 
                if nums[mid]>=x : 
                    r=mid-1 
                else : 
                    l=mid+1 
            return l 

        n=len(nums) 
        nums.sort() 
        ans=0 
        for i in range(n-2) : 
            for j in range(i+1, n-1) : 
                a=nums[i] 
                b=nums[j] 
                x=a+b 
                ans+=bSearch(nums, j+1, n-1, x)-j-1 
        return ans
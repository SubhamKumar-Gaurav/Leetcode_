class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums) 
        nums.sort()  
        ans=set() 
        for i in range(n-2) :
            x=-nums[i]
            j=i+1 
            k=n-1 
            while j<k : 
                if nums[j]+nums[k]==x : 
                    ans.add((nums[i], nums[j], nums[k]))
                    j+=1 
                    k-=1 
                elif nums[j]+nums[k]<x : 
                    j+=1 
                else :
                    k-=1 
            
        res=[] 
        for i in ans : 
            res.append(i)
        return res
class Solution:
    def findLHS(self, nums: List[int]) -> int: 
        d={} 
        for i in nums : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]=1 
        s=set() 
        arr=[] 
        for i in range(len(nums)) : 
            if nums[i] not in s : 
                s.add(nums[i])
                arr.append(nums[i]) 
        ans=0 
        arr.sort() 
        for i in range(len(arr)-1) : 
            if (arr[i+1]-arr[i])==1 : 
                temp=d[arr[i+1]]+d[arr[i]] 
                ans=max(ans, temp)
        return ans 
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def dig_sum(n) : 
            res=0 
            while n : 
                res+=n%10 
                n=n//10 
            return res 

        n=len(nums)
        l=defaultdict(list) 
        for i in nums : 
            l[dig_sum(i)].append(i)  
        ans=-1
        for i in l :
            l[i].sort() 
            if len(l[i])>=2 :  
                for j in range(len(l[i])-1) : 
                    temp=l[i][j]+l[i][j+1] 
                    ans=max(ans, temp) 
        return ans
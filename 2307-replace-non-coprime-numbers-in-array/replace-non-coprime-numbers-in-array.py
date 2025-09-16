
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]: 
        def gcd(a,b) : 
            if b==0 : 
                return a 
            return gcd(b, a%b) 
        
        n=len(nums)
        ans=[nums[0]] 
        for i in range(1,n) : 
            y=nums[i] 
            while len(ans)>0 and gcd(y, ans[-1]) >1 : 
                x=ans[-1] 
                ans.pop() 
                y=(x*y)//gcd(x,y) 
            ans.append(y) 
        return ans
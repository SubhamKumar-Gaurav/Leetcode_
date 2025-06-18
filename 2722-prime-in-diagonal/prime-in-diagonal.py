class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:  
        n=0 
        for i in range(len(nums)) : 
            n=max(n, max(nums[i]))

        prime=[True for i in range(n+1)] 
        prime[0]=False 
        prime[1]=False 
        p=2 
        while p*p<=n+1 : 
            if prime[p]==True : 
                for i in range(p*p, n+1, p) : 
                    prime[i]=False 
            p+=1 

        primes=set()
        for i in range(2, len(prime)) : 
            if prime[i] : 
                primes.add(i)

        ans=0 
        for i in range(len(nums)) : 
            if nums[i][i] in primes : 
                ans=max(ans, nums[i][i]) 
            if nums[i][len(nums)-i-1] in primes : 
                ans=max(ans, nums[i][len(nums)-i-1]) 
        return ans
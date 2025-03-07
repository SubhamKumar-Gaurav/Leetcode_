class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n) : 
            if n==1 : 
                return False 
            elif n==2 or n==3 : 
                return True 
            elif n%2==0 or n%3==0 : 
                return False 
            i=5 
            while i*i <= n : 
                if (n%i)==0 or (n%(i+2))==0 : 
                    return False 
                i+=6 
            return True 

        primes=[] 
        for i in range(left, right+1) : 
            if isPrime(i) : 
                primes.append(i) 
        if len(primes)<2 : 
            return [-1, -1]
        ans=[primes[0], primes[1]]
        res=primes[1]-primes[0] 
        for i in range(1, len(primes)-1) :
            diff=primes[i+1]-primes[i] 
            if diff<res : 
                res=diff 
                ans=[primes[i], primes[i+1]] 
        return ans
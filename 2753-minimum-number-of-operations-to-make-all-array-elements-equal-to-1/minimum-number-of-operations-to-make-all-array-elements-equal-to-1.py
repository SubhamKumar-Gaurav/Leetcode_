class Solution: 
    def minOperations(self, nums: List[int]) -> int: 
        def gcd(a, b) : 
            if b==0 : 
                return a 
            return gcd(b, a%b) 
        
        def gcdArr(arr) : 
            n=len(arr) 
            gcdVal=arr[0]
            for i in range(1, n) : 
                gcdVal=gcd(gcdVal, arr[i]) 
            return gcdVal 

        n=len(nums) 

        # count for the ones which are already present in the array
        one=0 
        for i in range(n) : 
            if nums[i]==1 : 
                one+=1  
        if one!=0 : 
            return n-one  

        # when all elements are same, then gcd will always be equal to that number
        if len(set(nums))==1 :    
            return -1 
        
        steps=float('inf') 
        for i in range(n-1) : 
            arr=[nums[i]] 
            for j in range(i+1, n) : 
                arr.append(nums[j]) 
                if gcdArr(arr)==1 : 
                    steps=min(steps, len(arr)-1) 
        if steps==float('inf') : 
            return -1 
        return steps+n-1 
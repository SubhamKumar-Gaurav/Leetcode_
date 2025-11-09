class Solution: 
    def countOperations(self, num1: int, num2: int) -> int: 
        def gcd(a,b, count) : 
            if b==0 : 
                return count 
            return gcd(b, a%b, count+(a//b)) 
        
        return gcd(num1, num2, 0)
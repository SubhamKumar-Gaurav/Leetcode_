class Solution: 
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int: 
        ans=numBottles 
        empty=numBottles 
        full=0 

        while full+empty>=numExchange : 
            ans+=1 
            empty-=numExchange  
            full+=1 
            numExchange+=1 
            
        return ans
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int: 
        l=1 
        r=min(ranks)*cars*cars 
        res=0 
        while l<=r : 
            m=(l+r)//2 
            temp=0 
            for i in ranks : 
                temp+=math.floor(math.sqrt(m/i))
            if temp>=cars : 
                res=m 
                r=m-1 
            else : 
                l=m+1
        return res 
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        c=n
        b=[True]*n 
        for i in range(n) : 
            temp=fruits[i] 
            for j in range(n) : 
                if b[j]==True : 
                    if baskets[j]>=temp : 
                        c-=1 
                        b[j]=False 
                        break 
        return c
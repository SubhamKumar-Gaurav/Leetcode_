class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff=(high-low)//2 
        if low%2==0 and high%2==0 : 
            return diff
        return diff+1
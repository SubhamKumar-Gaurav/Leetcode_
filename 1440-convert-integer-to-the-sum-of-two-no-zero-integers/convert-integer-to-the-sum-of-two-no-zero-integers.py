class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n+1) : 
            l=[i, n-i] 
            if "0" not in str(l[0]) and "0" not in str(l[1]) : 
                return l
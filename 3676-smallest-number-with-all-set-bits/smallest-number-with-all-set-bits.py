class Solution:
    def smallestNumber(self, n: int) -> int:
        b=bin(n)[2:] 
        if b.count("1")==len(b) : 
            return n
        return int("1"*len(b), 2)
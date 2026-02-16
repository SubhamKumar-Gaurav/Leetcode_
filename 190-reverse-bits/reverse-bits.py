class Solution:
    def reverseBits(self, n: int) -> int:
        b=bin(n)[2:] 
        new="0b"+b[::-1]  
        diff=34-len(new) 
        new+=diff*"0"
        return int(new, 2)
from math import comb 
from collections import Counter 

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:  
        M=1000000007 
        total_ways=maxValue 
        freq={num:1 for num in range(1,maxValue+1)} 

        for array_size in range(1, n) : 
            new_freq=Counter() 
            for base_value in freq : 
                for multiplier in range(2,maxValue//base_value+1) : 
                    combinations=comb(n-1, array_size) 
                    total_ways+=combinations*freq[base_value] 
                    new_freq[multiplier*base_value]+=freq[base_value] 
            freq=new_freq 
            total_ways%=M
        return total_ways 
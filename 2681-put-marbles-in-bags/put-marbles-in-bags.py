
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights)==k or k==1 : 
            return 0 
        arr=[] 
        for i in range(len(weights)-1) : 
            arr.append(weights[i]+weights[i+1]) 
        arr.sort() 
        i=k-1
        max_val=sum(arr[-i:])
        min_val=sum(arr[:i])
        return max_val-min_val
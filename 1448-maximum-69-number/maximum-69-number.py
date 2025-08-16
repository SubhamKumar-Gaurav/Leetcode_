class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num) 
        idx=None
        for i in range(len(s)) : 
            if s[i]=="6" : 
                idx=i 
                break 
        l=list(s)
        if idx is not None : 
            l[idx]="9" 
            return int("".join(l)) 
        return num
  
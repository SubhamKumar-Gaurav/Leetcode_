class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        extra=len(s)%k 
        if extra!=0 : 
            for i in range(k-extra) :
                s+=fill 

        arr=[] 
        for i in range(0,len(s),k) : 
            arr.append(s[i:i+k])
        return arr
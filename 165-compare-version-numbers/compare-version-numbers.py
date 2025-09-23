class Solution: 
    def compareVersion(self, version1: str, version2: str) -> int: 
        l1=list(version1.split(".")) 
        l2=list(version2.split(".")) 
        extra_len=max(len(l1), len(l2))-min(len(l1), len(l2))  
        if len(l1)>len(l2) : 
            for i in range(extra_len) : 
                l2.append("0") 
        elif len(l1)<len(l2) : 
            for i in range(extra_len) : 
                l1.append("0") 
        n=len(l1) 
        for i in range(n) : 
            if int(l1[i]) < int(l2[i]) : 
                return -1 
            elif int(l1[i]) > int(l2[i]) :
                return 1 
        return 0
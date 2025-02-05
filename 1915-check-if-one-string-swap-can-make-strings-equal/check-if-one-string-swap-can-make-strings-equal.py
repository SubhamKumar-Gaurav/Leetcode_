class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        l=[] 
        for i in range(len(s1)) : 
            if s1[i]!=s2[i] : 
                l.append(i) 
        if len(l)==0 : 
            return True 
        if len(l)!=2 : 
            return False 
        if s1[l[0]]==s2[l[1]] and s1[l[1]]==s2[l[0]] : 
            return True 
        else : 
            return False
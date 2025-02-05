class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal) : 
            return False
        if len(s)==1 :     
            return False 
        if len(s)==2 : 
            if s[0]==goal[1] and s[1]==goal[0] : 
                return True 
            else : 
                return False 
        else : 
            l=[]
            for i in range(len(s)) : 
                if s[i]!=goal[i] : 
                    l.append(i)
            if s==goal : 
                c=Counter(s)
                for i in c : 
                    if c[i]>=2 : 
                        return True 
                return False 
            if len(l)==2 :  
                if s[l[0]]==goal[l[1]] and s[l[1]]==goal[l[0]] : 
                    return True 
                return False 
            return False
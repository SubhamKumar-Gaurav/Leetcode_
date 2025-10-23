class Solution: 
    def isValid(self, s: str) -> bool: 
        st=list(s) 
        i=0 
        while len(st)>3 and i<len(st)-2 : 
            if st[i]=="a" and st[i+1]=="b" and st[i+2]=="c" : 
                st.pop(i) 
                st.pop(i) 
                st.pop(i) 
                if i>=2 : 
                    i-=2 
                else : 
                    i-=1 
            else :
                i+=1 
                
        if len(st)<3 : 
            return False 
        if st[0]=="a" and st[1]=="b" and st[2]=="c" : 
            return True 
        return False 
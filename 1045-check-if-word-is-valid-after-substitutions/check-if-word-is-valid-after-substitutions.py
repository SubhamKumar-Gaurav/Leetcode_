class Solution: 
    def isValid(self, s: str) -> bool: 
        st=[] 
        for i in s : 
            st.append(i) 
            if len(st)>=3 : 
                if st[-1]=="c" and st[-2]=="b" and st[-3]=="a" : 
                    st.pop() 
                    st.pop() 
                    st.pop() 
        if len(st)==0 : 
            return True 
        return False 
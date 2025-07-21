class Solution:
    def makeFancyString(self, s: str) -> str: 
        if len(s)<=2 : 
            return s 
        st=[]
        st.append(s[0]) 
        st.append(s[1]) 
        for i in range(2, len(s)) : 
            st.append(s[i])
            if st[-1]==st[-2] and st[-2]==st[-3] : 
                st.pop() 
        return "".join(st)
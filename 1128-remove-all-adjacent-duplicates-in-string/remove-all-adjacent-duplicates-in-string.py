class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[s[0]] 
        for i in range(1,len(s)) : 
            st.append(s[i]) 
            while len(st)>1 and st[-1]==st[-2] : 
                st.pop()
                st.pop() 
        return "".join(st) 
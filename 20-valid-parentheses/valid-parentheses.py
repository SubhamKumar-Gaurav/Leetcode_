class Solution:
    def isValid(self, s: str) -> bool:
        openBracket={"(", "[", "{" } 
        closeBracket={")", "]", "}" }
        st=[] 
        for i in s : 
            curr=i 
            if not st : 
                st.append(i) 
            else : 
                if i in openBracket :  
                    st.append(i) 
                else : 
                    if i==")" : 
                        if not st : 
                            return False 
                        elif st[-1]=="(" : 
                            st.pop() 
                        else : 
                            return False
                    elif i=="]" : 
                        if not st : 
                            return False 
                        elif st[-1]=="[" : 
                            st.pop() 
                        else : 
                            return False 
                    elif i=="}" : 
                        if not st : 
                            return False 
                        elif st[-1]=="{" : 
                            st.pop() 
                        else : 
                            return False 
        return len(st)==0 
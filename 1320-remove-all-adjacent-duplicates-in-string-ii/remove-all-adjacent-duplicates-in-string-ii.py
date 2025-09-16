
class Solution: 
    def removeDuplicates(self, s: str, k: int) -> str: 
        st=[] 
        for c in s : 
            if st and st[-1][0]==c : 
                st[-1][1]+=1 
            else : 
                st.append([c, 1]) 
            
            if st[-1][1]==k : 
                st.pop() 
        ans="" 
        for i, j in st : 
            ans+=i*j 
        return ans
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n=len(words) 
        st=[] 
        st.append(words[0]) 
        for i in range(1,n) : 
            j1="".join(sorted(st[-1])) 
            j2="".join(sorted(words[i])) 
            if j1!=j2 : 
                st.append(words[i]) 
        return st 
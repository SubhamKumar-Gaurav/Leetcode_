class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int: 
        n=len(colors) 
        st=[[colors[0], 0]]   
        ans=0 
        i=1 
        while i<n : 
            if len(st)==0 : 
                st.append([colors[i], i]) 
            else : 
                if st[-1][0]==colors[i] : 
                    a=neededTime[st[-1][1]] 
                    b=neededTime[i] 
                    if a<b : 
                        st.pop() 
                        st.append([colors[i], i]) 
                        ans+=a 
                    else : 
                        ans+=b  
                else : 
                    st.append([colors[i], i]) 
            i+=1 

        return ans 
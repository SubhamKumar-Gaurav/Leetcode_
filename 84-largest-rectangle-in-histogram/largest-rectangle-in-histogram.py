class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights) 
        st=[] 
        res=0 
        for i in range(n) :
            while st and heights[st[-1]]>=heights[i] : 
                tp=st[-1] 
                st.pop() 
                if st : 
                    curr_width=(i-st[-1]-1)
                else : 
                    curr_width=i 
                res=max(res, curr_width*heights[tp]) 
            st.append(i)
        while st : 
            tp=st[-1]
            st.pop() 
            if st : 
                curr_width=(n-st[-1]-1) 
            else : 
                curr_width=n 
            res=max(res, curr_width*heights[tp]) 
        return res 
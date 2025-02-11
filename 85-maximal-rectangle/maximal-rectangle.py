class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows=len(matrix) 
        cols=len(matrix[0]) 
        for r in range(rows) : 
            for c in range(cols) : 
                matrix[r][c]=1 if matrix[r][c]=="1" else 0 

        def maxArea(arr) :  # Largest area Histogram 
            n=len(arr) 
            st=[] 
            res=0 
            for i in range(n) : 
                while st and arr[st[-1]]>=arr[i] : 
                    tp=st[-1] 
                    st.pop() 
                    if st : 
                        curr_width=(i-st[-1]-1) 
                    else : 
                        curr_width=i 
                    res=max(res, curr_width*arr[tp]) 
                st.append(i) 
            while st : 
                tp=st[-1] 
                st.pop() 
                if st : 
                    curr_width=(n-st[-1]-1)
                else : 
                    curr_width=n 
                res=max(res, curr_width*arr[tp])
            return res 
        
        ans=maxArea(matrix[0]) 
        for r in range(1, rows) : 
            for c in range(cols) : 
                if matrix[r][c] : 
                    matrix[r][c]+=matrix[r-1][c] 
            ans=max(ans, maxArea(matrix[r]))
        return ans 
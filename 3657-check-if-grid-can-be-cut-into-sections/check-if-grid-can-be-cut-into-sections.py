class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:  
        x_arr=[]
        y_arr=[]
        for i in range(len(rectangles)) : 
            x_arr.append([rectangles[i][0], rectangles[i][2]])  
            y_arr.append([rectangles[i][1], rectangles[i][3]]) 
        x_arr.sort(key=lambda x: x[0])
        y_arr.sort(key=lambda x: x[0]) 
        vc=0 
        prev_end=-1 
        for start, end in x_arr : 
            if prev_end<=start : 
                vc+=1 
            prev_end=max(prev_end, end) 
        if vc>=3 : 
            return True 

        hc=0
        prev_end=-1  
        for start, end in y_arr : 
            if prev_end<=start  : 
                hc+=1 
            prev_end=max(prev_end, end)
        if hc>=3 : 
            return True 
            
        return False 
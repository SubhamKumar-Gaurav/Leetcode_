class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n=len(points) 
        area=0 
        for i in range(n) : 
            x1=points[i][0]
            y1=points[i][1]
            for j in range(i+1, n) :
                x2=points[j][0]
                y2=points[j][1] 
                for k in range(j+1, n) : 
                    x3=points[k][0] 
                    y3=points[k][1] 

                    curr_area=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2 
                    area=max(area, curr_area) 
        return area 
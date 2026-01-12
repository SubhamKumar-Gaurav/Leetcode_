class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n=len(points) 
        res=0 
        for i in range(1, n) : 
            dx=abs(points[i-1][0]-points[i][0]) 
            dy=abs(points[i-1][1]-points[i][1]) 
            res+=max(dx, dy) 
        return res 
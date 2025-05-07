import heapq 
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int: 
        m=len(moveTime)
        n=len(moveTime[0])  
        directions=[(1,0), (-1,0), (0,1), (0,-1)] 
        res=[[float("inf") for _ in range(n)] for _ in range(m)] 
        pq=[] 

        res[0][0]=0  
        heapq.heappush(pq,(0,0,0)) 

        while pq :
            currTime,i,j=heapq.heappop(pq)
            if i==m-1 and j==n-1 :
                return currTime 
            for dx,dy in directions : 
                new_i, new_j = i+dx , j+dy 
                if 0<=new_i<m and 0<=new_j<n : 
                    wait=max(moveTime[new_i][new_j]-currTime,0) 
                    arrTime=currTime+wait+1   
                    if res[new_i][new_j]>arrTime :
                        res[new_i][new_j]=arrTime 
                        heapq.heappush(pq, (arrTime, new_i, new_j))

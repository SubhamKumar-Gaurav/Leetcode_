from heapq import heapify, heappush, heappop

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n=len(events)
        events.sort(key=lambda x: (x[0], x[1]))  
        pq=[] 
        heapify(pq) 
        ans=0 
        day=events[0][0] 
        i=0 
        while i<n or pq : 
            if pq is None : 
                day=events[i][0] 
            while i<n and events[i][0]==day : 
                heappush(pq, events[i][1])
                i+=1 
            if pq : 
                heappop(pq) 
                ans+=1 
            day+=1 
            while pq and pq[0]<day : 
                heappop(pq) 
        return ans
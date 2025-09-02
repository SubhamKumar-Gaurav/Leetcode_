from heapq import heappush, heappop 
class Solution: 
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float: 
        def gain(pss, tot) : 
            return ((pss+1)/(tot+1))-(pss/tot) 

        pq=[] 
        ans=0 
        for pss, tot in classes : 
            ans+=pss/tot 
            heappush(pq, (-gain(pss,tot), pss, tot)) 
        
        for _ in range(extraStudents) : 
            curr_gain, pss, tot = heappop(pq)
            ans-=pss/tot 
            pss+=1 
            tot+=1 
            ans+=pss/tot
            heappush(pq, (-gain(pss, tot), pss, tot)) 
        return ans/len(classes)
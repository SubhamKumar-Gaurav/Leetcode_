from collections import defaultdict  

class Solution:
    def edgeScore(self, edges: List[int]) -> int: 
        graph=[] 
        for i in range(len(edges)) : 
            graph.append([i, edges[i]]) 

        d=defaultdict(int) 
        for u,v in graph : 
            d[v]+=u 

        arr=[] 
        for i in d : 
            arr.append([i, d[i]]) 
        
        arr.sort(key=lambda x: (-x[1], x[0]))
        
        return arr[0][0]
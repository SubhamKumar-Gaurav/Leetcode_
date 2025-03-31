class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights)==k or k==1 : 
            return 0 
        min_heap=[]  
        max_heap=[] 
        for i in range(len(weights)-1) : 
            min_heap.append(weights[i]+weights[i+1]) 
            max_heap.append(-weights[i]-weights[i+1])
        heapify(min_heap) 
        heapify(max_heap)
        min_val=0 
        max_val=0  
        for i in range(k-1) : 
            min_val+=heappop(min_heap) 
            max_val+=(-heappop(max_heap))
        return max_val-min_val
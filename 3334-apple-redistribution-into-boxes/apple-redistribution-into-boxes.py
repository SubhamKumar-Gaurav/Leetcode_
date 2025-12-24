class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n=len(capacity) 
        capacity.sort(reverse=True) 
        total=sum(apple)
        i=0 
        while total>0 and i<n : 
            if total<=capacity[i] : 
                total=0 
                i+=1 
            elif total>capacity[i] : 
                total-=capacity[i] 
                i+=1  
        return i
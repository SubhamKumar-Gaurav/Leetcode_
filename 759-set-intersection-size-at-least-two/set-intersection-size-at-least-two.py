
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # sort ascending - right value , descending - left value 
        intervals.sort(key=lambda x: (x[1], -x[0])) 
        
        numsSet=set() 
        a=-1 
        b=-1 
        i=0 
        while i<len(intervals) :   
            if b<intervals[i][0] : 
                a=intervals[i][1]-1
                b=intervals[i][1] 
            elif a<intervals[i][0] : 
                a=b 
                b=intervals[i][1] 
            numsSet.add(a)  
            numsSet.add(b)
            i+=1 

        return len(numsSet) 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort(key=lambda x: x[0]) 
        res=0 
        for i in range(1,n) : 
            if intervals[res][1]>=intervals[i][0] : 
                intervals[res][1]=max(intervals[res][1], intervals[i][1]) 
            else : 
                res+=1 
                intervals[res]=intervals[i] 
        ans=[]
        for i in range(res+1) : 
            ans.append(intervals[i]) 
        return ans
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int: 
        meetings.sort(key= lambda x: x[0])
        res=0 
        for i in range(1,len(meetings)) : 
            if meetings[res][1]>=meetings[i][0] : 
                meetings[res][1]=max(meetings[res][1], meetings[i][1]) 
            else : 
                res+=1 
                meetings[res]=meetings[i] 
        ans=0 
        ans+=(meetings[0][0]-1)
        for i in range(res) : 
            ans+=(meetings[i+1][0]-(meetings[i][1]+1))
        ans+=(days-meetings[res][1])
        return ans
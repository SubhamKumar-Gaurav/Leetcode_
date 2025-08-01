from collections import defaultdict 
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:   
        d=defaultdict(list) 
        for i in range(len(groupSizes)) :  
            d[groupSizes[i]].append(i) 
    
        ans=[] 
        for i in d : 
            j=0 
            for k in range(len(d[i])//i) :  
                temp=d[i][j:j+i] 
                ans.append(temp) 
                j+=i 
        return ans
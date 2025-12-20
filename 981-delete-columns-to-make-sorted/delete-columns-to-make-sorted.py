class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        arr=[] 
        for i in range(len(strs[0])) : 
            temp=[] 
            for j in range(len(strs)) : 
                temp.append(strs[j][i]) 
            arr.append(temp) 
        
        deletion=0 
        for i in range(len(arr)) : 
            if arr[i]!=sorted(arr[i]) : 
                deletion+=1 
        return deletion 
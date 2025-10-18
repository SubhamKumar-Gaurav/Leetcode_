from collections import defaultdict 

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int: 
        d=defaultdict(int)
        for i in arr : 
            d[i]+=1 

        freq_arr=[] 
        for i in d : 
            freq_arr.append([i, d[i]]) 
        
        freq_arr.sort(key=lambda x: x[1]) 

        i=0 
        while k>0 and i<len(freq_arr) : 
            curr_freq=freq_arr[i][1] 
            if curr_freq>=k :     
                freq_arr[i][1]-=k
                k=0 
            else : 
                freq_arr[i][1]=0  
                k-=curr_freq 
            i+=1 

        ans=0 
        for val, freq in freq_arr : 
            if freq>0 : 
                ans+=1 
        return ans 
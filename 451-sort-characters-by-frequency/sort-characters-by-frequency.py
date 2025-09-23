class Solution: 
    def frequencySort(self, s: str) -> str: 
        d={} 
        for i in s : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]=1 
        arr=[] 
        for i in d : 
            arr.append([d[i], i]) 
        arr.sort(reverse=True, key=lambda x: x[0]) 
         
        ans="" 
        for i in range(len(arr)) : 
            ans+=arr[i][1]*arr[i][0] 
        
        return ans
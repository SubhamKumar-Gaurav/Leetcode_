class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        d={} 
        for i in nums : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]=1 
        arr=[] 
        for i in d : 
            arr.append([i, d[i]]) 
        
        arr.sort(reverse=True, key=lambda x: x[1]) 

        ans=[] 
        for i in range(k) : 
            ans.append(arr[i][0]) 
        return ans
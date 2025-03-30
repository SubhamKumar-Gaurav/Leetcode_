class Solution:
    def partitionLabels(self, s: str) -> List[int]: 
        d=defaultdict(list) 
        for i in s : 
            d[i]=[float('inf'), float("-inf")] 
        for i in range(len(s)) : 
            d[s[i]][0]=min(i, d[s[i]][0])
            d[s[i]][1]=max(i, d[s[i]][1]) 
        arr=[] 
        for i in d : 
            arr.append(d[i])
        arr.sort(key= lambda x: x[0])
        prev=0 
        for curr in range(1,len(arr)) : 
            if arr[prev][1]>=arr[curr][0] : 
                arr[prev][1]=max(arr[prev][1], arr[curr][1]) 
            else : 
                prev+=1 
                arr[prev]=arr[curr] 
        new_arr=[] 
        for i in range(prev+1) : 
            new_arr.append(arr[i]) 
        res=[]
        for i,j in new_arr : 
            res.append(j-i+1) 
        return res 
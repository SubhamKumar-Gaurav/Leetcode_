class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int: 
        if len(arr)==3 : 
            if arr[0]+arr[1] != arr[2] : 
                return 0
        s=set(arr) 
        res=0 
        for i in range(len(arr)-1) :  
            for j in range(i+1, len(arr)) : 
                temp=[arr[i], arr[j]]
                curr=0
                while True : 
                    if (temp[-1]+temp[-2]) in s : 
                        curr+=1 
                        res=max(res, curr)  
                        temp.append(temp[-1]+temp[-2])
                    else : 
                        break 
        return res+2 if res else 0
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0 
        arr=[] 
        for i in bank : 
            if i.count("1")>0 : 
                arr.append(i) 
        m=len(arr)  
        for i in range(m-1) : 
            ans+=(arr[i].count("1")*arr[i+1].count("1")) 
        return ans
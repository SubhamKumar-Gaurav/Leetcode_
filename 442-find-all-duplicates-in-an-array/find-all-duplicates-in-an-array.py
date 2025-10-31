class Solution: 
    def findDuplicates(self, nums: List[int]) -> List[int]: 
        n=len(nums) 
        arr=[0]*(n+2)  
        for i in nums : 
            arr[i]+=1 
        
        i=0
        j=0 
        while j<len(arr) :  
            if arr[j]==2 : 
                arr[i]=j 
                i+=1 
            j+=1 
        if i==0 : 
            return [] 
        return arr[:i]
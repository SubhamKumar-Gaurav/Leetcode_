from collections import defaultdict 

class Solution: 
    def findSmallestInteger(self, nums: List[int], value: int) -> int: 
        d=defaultdict(int) 
        n=len(nums) 
        for i in range(n) : 
            idx=nums[i]%value 
            d[idx]+=1 
        
        s=set() 
        for i in d : 
            for j in range(d[i]) : 
                temp=i+(j*value) 
                s.add(temp) 
        arr=[] 
        for i in s : 
            arr.append(i) 
        arr.sort() 
        for i in range(len(arr)) : 
            if i!=arr[i] : 
                return i 
        return n
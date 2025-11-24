class Solution: 
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:   
        arr=[]
        a="" 
        n=len(nums)
        for i in range(n) : 
            a+=str(nums[i]) 
            x=int(a, 2) 
            if x%5==0 : 
                arr.append(True) 
            else : 
                arr.append(False) 
        return arr 
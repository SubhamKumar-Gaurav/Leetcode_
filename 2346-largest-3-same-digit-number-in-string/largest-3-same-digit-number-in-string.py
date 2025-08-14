class Solution:
    def largestGoodInteger(self, num: str) -> str:   
        arr=[]
        n=len(num)
        for i in range(n-2) : 
            if num[i]==num[i+1] and num[i+1]==num[i+2] : 
                arr.append(num[i:i+3]) 
        if arr : 
            arr.sort() 
            return arr[-1] 
        return ""
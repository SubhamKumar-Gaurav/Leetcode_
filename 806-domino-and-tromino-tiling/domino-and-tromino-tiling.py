class Solution:
    def numTilings(self, n: int) -> int:  
        if n<=2 : 
            return n 
        arr=[1]*(n+1) 
        arr[1]=1 
        arr[2]=2 
        arr[3]=5 
        for i in range(4,n+1) : 
            arr[i]=(2*arr[i-1] + arr[i-3])%1000000007
        return arr[n]
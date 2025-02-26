class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:  
        n=len(arr)
        prefixSum=[0]*(n)
        prefixSum[0]=arr[0]
        c=0
        for i in range(1,n) : 
            prefixSum[i] = prefixSum[i-1]+arr[i] 
        odd_count=0 
        even_count=1 
        for i in range(len(prefixSum)) : 
            if prefixSum[i]%2==1 : 
                odd_count+=1 
                c+=even_count
            else : 
                even_count+=1 
                c+=odd_count
        return c%((10**9)+7) 
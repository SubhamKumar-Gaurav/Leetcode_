class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int: 
        n=len(colors) 
        ans=0 
        alt=1
        prev=colors[0] 
        for i in range(1, n+k-1 ) : 
            i0=i%n 
            if prev==colors[i0] : 
                alt=1 
            else : 
                alt+=1 
            ans+=(alt>=k) 
            prev=colors[i0]
        return ans 
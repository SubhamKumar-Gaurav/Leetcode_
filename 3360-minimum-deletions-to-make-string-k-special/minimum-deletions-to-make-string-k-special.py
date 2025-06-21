
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:  
        d={} 
        for i in word : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]= 1
        freq=[] 
        for i in d : 
            freq.append(d[i]) 
        freq.sort() 
        n=len(freq)

        prefix=[0]*(n+1) 
        for i in range(n) : 
            prefix[i+1]=prefix[i]+freq[i] 
        
        total=prefix[-1]
        ans=float("inf") 
        for i in range(n) : 
            target=freq[i] 
            max_allowed=target+k 

            j=n 
            for idx in range(i, n) : 
                if freq[idx]>max_allowed : 
                    j=idx 
                    break 
            delete_below=prefix[i]
            delete_above=total-prefix[j]-(max_allowed*(n-j)) 
            total_deletions=delete_below + delete_above 
            ans=min(ans, total_deletions) 
        return ans
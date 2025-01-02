class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels={"a", "e", "i", "o", "u"}
        prefixSum=[0]*(len(words)+1)
        prefixSum[0]=0 
        for i in range(len(words)) :  
            prefixSum[i+1]=prefixSum[i]
            if words[i][0] in vowels and words[i][-1] in vowels : 
                prefixSum[i+1]+=1 

        res=[]
        for q in queries :  
            ans=prefixSum[q[1]+1]-prefixSum[q[0]]     
            res.append(ans) 
        return res
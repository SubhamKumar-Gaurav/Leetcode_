class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr=set()
        n=len(words)
        for i in range(n) :  
            w=words[i]
            c=1 
            for j in range(n) : 
                if w in words[j] and i!=j : 
                    arr.add(w)
        res=[]
        for i in arr : 
            res.append(i)
        return res                
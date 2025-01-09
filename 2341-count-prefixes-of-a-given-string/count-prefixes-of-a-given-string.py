class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c=0 
        for i in range(len(words)) : 
            if s.startswith(words[i]) : 
                c+=1 
        return c
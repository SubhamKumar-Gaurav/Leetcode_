class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_index=[] 
        vowels=[] 
        for i in range(len(s)) : 
            if s[i] in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"} : 
                vowel_index.append(i) 
                vowels.append(s[i]) 
        if len(vowels)==0 : 
            return s
        vowels.sort() 
        l=list(s)
        c=0 
        for i in range(len(l)) : 
            if c<len(vowel_index) and i==vowel_index[c] : 
                l[i]=vowels[c] 
                c+=1 
        return "".join(l) 
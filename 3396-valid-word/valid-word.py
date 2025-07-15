class Solution:
    def isValid(self, word: str) -> bool: 
        if len(word)<3 : 
            return False 
        vowels={"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"} 
        consonants={"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"}
        # nums={'0','1','2','3','4','5','6','7','8','9'}
        c1=False 
        c2=False 
        c3=False
        for i in word : 
            if i in vowels : 
                c2=True 
            elif i in consonants : 
                c3=True 
            elif 48<=ord(i)<=57 : 
                c1=True 
            else : 
                return False
        return c2 and c3
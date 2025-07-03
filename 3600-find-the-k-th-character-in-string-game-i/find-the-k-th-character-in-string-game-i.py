class Solution:
    def kthCharacter(self, k: int) -> str:  
        word="a" 
        while True : 
            while len(word)<k : 
                length=len(word)
                temp=""
                for i in range(length) : 
                    curr=word[i]
                    temp+=chr(((ord(curr)-ord("a")+1)%26)+ord("a")) 
                word+=temp 
            break 
        return word[k-1]
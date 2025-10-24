class Solution: 
    def nextBeautifulNumber(self, n: int) -> int: 
        def numCheck(n) : 
            s=str(n) 
            for i in s : 
                if s.count(i)!=int(i) : 
                    return False 
            return True 

        i=n+1 
        while True : 
            if numCheck(i) :
                break  
            i+=1  
        return i 
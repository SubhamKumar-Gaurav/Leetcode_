class Solution:
    def sumZero(self, n: int) -> List[int]:
        i=1 
        j=-1 
        arr=[0] if n%2 else [] 
        for _ in range(n//2) :
            arr.append(i)
            arr.append(j)
            i+=1 
            j-=1 
        return arr 
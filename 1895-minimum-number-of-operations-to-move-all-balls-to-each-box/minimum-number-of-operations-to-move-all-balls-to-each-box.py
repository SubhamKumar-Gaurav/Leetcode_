class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        arr=[] 
        for i in range(n) :
            temp=0  
            for j in range(n) : 
                if boxes[j]=="1" and i!=j : 
                    temp+=abs(i-j) 
            arr.append(temp)
        return arr
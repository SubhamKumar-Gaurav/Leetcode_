
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes) 
        res=[0]*n 
        balls=0 
        moves=0 
        for i in range(n) : 
            res[i] = balls + moves 
            moves = moves + balls 
            balls += int(boxes[i])

        balls=0 
        moves=0 
        for i in reversed(range(n)) : 
            res[i]+= balls + moves 
            moves = moves + balls 
            balls += int(boxes[i])
        return res 
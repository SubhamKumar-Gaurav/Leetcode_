class Solution:
    def countTriples(self, n: int) -> int:
        s=set() 
        for i in range(1, n+1) : 
            for j in range(1, n+1) : 
                lhs=(i*i)+(j*j) 
                rhs=math.sqrt(lhs)
                if rhs==int(rhs) and int(rhs)<=n : 
                    s.add((i, j, int(rhs))) 
        return len(s)
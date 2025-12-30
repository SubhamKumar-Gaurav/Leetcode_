class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def magic(A) :
            all_nums=set()
            for i in A :
                all_nums.update(i)  
            if all_nums != set(range(1,10)) :
                return False       
            r=[sum(row) for row in A] 
            c=[sum(A[i][j] for i in range(3)) for j in range(3)]    
            d1=A[0][0]+A[1][1]+A[2][2] 
            d2=A[0][2]+A[1][1]+A[2][0] 
            return (r[0]==r[1]==r[2]==c[0]==c[1]==c[2]==d1==d2==15)  

        c=0 
        for i in range(len(grid)-2)  :
            for j in range(len(grid[0])-2) :
                subgrid=[row[j:j+3] for row in grid[i:i+3]] 
                if magic(subgrid) :
                    c+=1 
        return c                 
                
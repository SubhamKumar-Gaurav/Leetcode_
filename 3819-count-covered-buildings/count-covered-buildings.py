from collections import defaultdict 
class Solution: 
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int: 
        buildings.sort(key=lambda x: (x[0], x[1])) 
        rows=defaultdict(list) 
        cols=defaultdict(list) 

        for i, j in buildings :   # buildings are stored in rows and cols 
            rows[i].append(j) 
            cols[j].append(i) 
        
        # sort the rows and cols list 
        for i in rows : 
            rows[i].sort() 
        for j in cols :
            cols[j].sort() 
        
        # if the curr building is neither first or last in that row and column, then obviously there exists some buildings on both the sides, we use two variables- one to check the rowWise and the other to check columnWise
        ans=0 
        for i, j in buildings : 
            rowWise=False 
            colWise=False 
            if rows[i][0]!=j and rows[i][-1]!=j : 
                rowWise=True 
            if cols[j][0]!=i and cols[j][-1]!=i : 
                colWise=True 
            if rowWise and colWise : 
                ans+=1 
        return ans 
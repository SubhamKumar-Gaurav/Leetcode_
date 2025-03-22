
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:  
        def dfs(v, res) : 
            if v in visited : 
                return 
            visited.add(v) 
            res.append(v) 
            for u in adj[v] : 
                dfs(u, res)
            return res 

        adj=defaultdict(list) 
        for v1,v2 in edges : 
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        res=0 
        visited=set() 
        for v in range(n) : 
            if v in visited : 
                continue 
            component=dfs(v, []) 
            if all([len(component)-1 == len(adj[v2]) for v2 in component]) :
                res+=1 
        return res 
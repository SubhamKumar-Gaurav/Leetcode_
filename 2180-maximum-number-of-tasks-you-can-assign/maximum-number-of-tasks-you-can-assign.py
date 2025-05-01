from collections import deque 
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:  
        tasks.sort() 
        workers.sort() 
        def ans(mid, pills) : 
            n=len(workers) 
            i=0 
            q=deque() 
            for j in range(n-mid, n) : 
                w=workers[j] 
                while i<mid and tasks[i]<=w+strength : 
                    q.append(tasks[i]) 
                    i+=1 
                if not q : 
                    return False 
                if q[0]<=w : 
                    q.popleft() 
                else : 
                    if pills==0 : 
                        return False 
                    pills-=1 
                    q.pop() 
            return True 

        l=0 
        r=min(len(tasks), len(workers)) 
        while l<r : 
            m=(l+r+1)//2 
            if ans(m, pills) : 
                l=m
            else : 
                r=m-1 
        return l
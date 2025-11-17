from collections import defaultdict 

class Solution: 
    def taskSchedulerII(self, tasks: List[int], space: int) -> int: 
        n=len(tasks) 

        d=defaultdict(list)
        days=0
        for i in range(n) : 
            if tasks[i] not in d : 
                days+=1 
                d[tasks[i]].append(days)  
            else : 
                if days-d[tasks[i]][-1] > space : 
                    days+=1 
                else : 
                    diff=space-(days-d[tasks[i]][-1]) 
                    days+=diff+1 
                d[tasks[i]].append(days)  
                 
        return days 
from collections import deque 

class Solution: 
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int: 
        n=len(students) 
        m=len(sandwiches) 

        if students==sandwiches : 
            return 0 

        students=deque(students) 
        eat=0 
        idx=0 
        zeroStd=students.count(0) 
        oneStd=students.count(1) 
        zeroSnd=sandwiches.count(0) 
        oneSnd=sandwiches.count(1) 
        rotations=0 
        
        while idx<m : 
            if students[0]==sandwiches[idx] : 
                eat+=1 
                if students[0]==0 : 
                    zeroStd-=1 
                    zeroSnd-=1 
                else : 
                    oneStd-=1 
                    oneSnd-=1 
                students.popleft() 
                idx+=1
                rotations=0  
            else :  
                temp=students.popleft()
                students.append(temp) 
                rotations+=1 

                if rotations==m : 
                    return n-eat 
        return n-eat 
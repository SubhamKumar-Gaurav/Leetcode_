class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]: 
        nums.sort() 
        arr=[] 
        for i in range(0,len(nums), 3) : 
            arr.append([nums[i], nums[i+1], nums[i+2]])  
        
        for i in range(len(arr)) : 
            if abs(arr[i][0]-arr[i][1])>k or abs(arr[i][0]-arr[i][2])>k or abs(arr[i][2]-arr[i][1])>k : 
                return [] 
        return arr
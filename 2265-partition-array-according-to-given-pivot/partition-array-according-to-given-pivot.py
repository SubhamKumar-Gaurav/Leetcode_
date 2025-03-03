class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]: 
        before=[] 
        mid=[] 
        after=[] 
        for i in range(len(nums)) : 
            if nums[i]<pivot : 
                before.append(nums[i])
            elif nums[i]==pivot : 
                mid.append(nums[i])
            else : 
                after.append(nums[i])
        return before+mid+after
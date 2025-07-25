from collections import defaultdict 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        d=defaultdict(list) 
        for i in range(len(nums)) : 
            d[nums[i]].append(i) 
        for i in range(len(nums)) : 
            if target-nums[i] in d : 
                if target-nums[i] == nums[i] : 
                    if len(d[target-nums[i]])>1 : 
                        return [i, d[target-nums[i]][1]] 
                    else : 
                        continue 
                else : 
                    return [i, d[target-nums[i]][0]]  
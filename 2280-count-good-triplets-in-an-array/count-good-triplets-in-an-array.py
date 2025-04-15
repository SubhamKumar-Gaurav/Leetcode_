from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:   
        index_map={num: i for i, num in enumerate(nums2)} 
        indices=[index_map[num] for num in nums1] 
        left_counts=[] 
        left_sorted=SortedList() 
        for idx in indices : 
            left_counts.append(left_sorted.bisect_left(idx)) 
            left_sorted.add(idx) 
        right_counts=[] 
        right_sorted=SortedList() 
        for idx in reversed(indices) : 
            right_counts.append(len(right_sorted)-right_sorted.bisect_right(idx)) 
            right_sorted.add(idx) 
        right_counts.reverse() 

        count=0 
        for i,j in zip(left_counts, right_counts) : 
            count+=i*j 
        return count
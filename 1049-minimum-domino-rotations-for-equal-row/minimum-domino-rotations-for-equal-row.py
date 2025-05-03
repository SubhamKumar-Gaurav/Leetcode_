class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:  
        same=Counter() 
        top_count=Counter(tops)
        bot_count=Counter(bottoms) 

        for a,b in zip(tops, bottoms) : 
            if a==b : 
                same[a]+=1 

        for i in range(1, 7) : 
            if top_count[i]+bot_count[i]-same[i] == len(tops) : 
                return min(top_count[i], bot_count[i])-same[i] 
        return -1
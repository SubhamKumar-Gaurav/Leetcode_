from collections import defaultdict 

class Solution: 
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]: 
        players=set() 
        loss=defaultdict(int) 
        for winner, loser in matches : 
            players.add(winner) 
            players.add(loser) 
            loss[loser]+=1 
        
        zero_loss=[] 
        one_loss=[] 

        for player in players : 
            if player not in loss : 
                zero_loss.append(player) 
            elif loss[player]==1 : 
                one_loss.append(player)  
        zero_loss.sort() 
        one_loss.sort() 

        ans=[] 
        ans.append(zero_loss)
        ans.append(one_loss) 
        return ans 
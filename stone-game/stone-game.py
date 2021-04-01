class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        left,right = 0,len(piles)-1
        Alex = Lee = 0
        chance = flag = 0
        while left < right:
            temp = 0
            if chance == 0:
                # give to ALex
                temp = max(piles[left],piles[right])
                Alex+=temp
                chance = 1
            else:
                # give to Lee
                temp = max(piles[left],piles[right])
                Lee+=temp
                chance = 0

            if temp == piles[left]:
                    flag = 1

            if flag==1:
                left+=1
            else:
                right-=1

            if Alex > Lee:
                return True
            return False
            
    
        
        
        
        
        
        
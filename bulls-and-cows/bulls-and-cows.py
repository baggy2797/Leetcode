class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        h = defaultdict(int)
        temp = list(zip(secret,guess))
        for t in range(len(temp)):
            if temp[t][0] == temp[t][1]:
                bulls+=1
            else:
                cows+= (h[temp[t][1]] < 0) + ( h[temp[t][0]] > 0)
                h[temp[t][1]]+=1
                h[temp[t][0]]-=1
        
        return str(bulls)+"A"+str(cows)+"B"
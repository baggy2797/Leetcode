class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        # pass
        length = len(currentState)
        res = []
        
        for i in range(1,length):
            new = currentState
            temp = ""
            if currentState[i] == currentState[i-1]:
                if currentState[i] == "+":
                    temp += new[:i-1]+"--"+new[i+1:]
                    res.append(temp)
        return res
        
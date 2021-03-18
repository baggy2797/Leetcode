class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = ["()"]
        for _ in range(n-1):
            r = [i[0:j+1]+"()"+i[j+1:] for i in r for j in range(len(i))]
            r = list(dict.fromkeys(r))
        return r
        
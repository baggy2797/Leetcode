class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tr = []
        for i in range(numRows):
            tr.append([])
            for j in range(i+1):
                if j == 0 or i == j:
                    tr[i].append(1)
                else:
                    tr[i].append(tr[i-1][j-1]+tr[i-1][j])
        return tr
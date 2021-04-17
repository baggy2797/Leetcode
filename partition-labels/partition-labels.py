class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        frequency = Counter(S)
        new = ""
        seen = set()
        res = []
        flag = 0
        for idx,element in enumerate(S):
            # print(element,frequency[element])
            if frequency[element]!=0:
                seen.add(element)
                new+=element
                frequency[element]-=1
            for x in seen:
                if frequency[x]==0:
                    flag = 1
                else:
                    flag = 0
                    break
            # print(frequency)
            if flag!=0:
                seen = set()
                res.append(len(new))
                new = ""
                flag =0
        return (res)
        
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # print(groupSizes)
        temp = collections.defaultdict(list)
        for k,v in enumerate(groupSizes):
            # print(temp)
            if v in temp:
                if len(temp[v][-1]) == v:
                    temp[v].append([k])
                else:
                    temp[v][-1].append(k)
            else:
                temp[v] = [[k]]
        res = []
        for i in temp.values():
            res.extend(i)
        
        return (res)
            
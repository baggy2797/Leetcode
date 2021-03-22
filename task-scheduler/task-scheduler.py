class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dicti = {}
        for task in tasks:
            if task not in dicti:
                dicti[task] = 1
            else:
                dicti[task] = dicti[task]+1
        
        vals = list(dicti.values())
        maxi = max(vals)
        
        num_most = len([i for i, v in dicti.items() if v == maxi])
        time = (maxi - 1) * (n + 1) + num_most
        return max(time, len(tasks))

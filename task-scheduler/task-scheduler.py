class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dicti = {}
        for task in tasks:
            if task not in dicti:
                dicti[task] = 1
            else:
                dicti[task] = dicti[task]+1
        
        maxi = max(list(dicti.values()))
        most = 0
        for key in dicti.keys():
            if dicti[key] == maxi:
                most = most+1
        
        time = (maxi - 1) * (n + 1) + most
        return max(time, len(tasks))

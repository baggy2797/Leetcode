class LogSystem:

    def __init__(self):
        self.logStorage = defaultdict(list)

    def put(self, id: int, timestamp: str) -> None:
        self.logStorage[timestamp] += [id]

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res = []
        idx = -1
        if granularity =="Year":
            h1,h2 = start.split(":"),end.split(":")
            h1,h2 = h1[:1],h2[:1]
            idx= 0
        elif granularity =="Month":
            h1,h2 = start.split(":"),end.split(":")
            h1,h2 = h1[:2],h2[:2]
            idx= 1
        elif granularity =="Day":
            h1,h2 = start.split(":"),end.split(":")
            h1,h2 = h1[:3],h2[:3]
            idx= 2
        elif granularity =="Hour":
            h1,h2 = start.split(":"),end.split(":")
            h1,h2 = h1[:4],h2[:4]
            idx= 3
        elif granularity =="Minute":
            h1,h2 = start.split(":"),end.split(":")
            h1,h2 = h1[:5],h2[:5]
            idx= 4
        elif granularity =="Second":
            h1,h2 = start.split(":"),end.split(":")
            h1,h2 = h1[:6],h2[:6]
            idx= 5
        
        start_time = int("".join(h1))
        end_time = int("".join(h2))
        
        for key,value in self.logStorage.items():
            holder = key.split(":")
            temp = "".join(holder[:idx+1])
            if int(temp) >= start_time and int(temp)<=end_time:
                res.append(value[0])
        return res
            

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
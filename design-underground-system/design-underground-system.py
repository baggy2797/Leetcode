class UndergroundSystem:

    def __init__(self):
        # self.start = {}
        # self.end = {}
        self.station_in_out_details = {}
        self.details= {}
        
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # if stationName not in self.start:
        #     self.start[stationName] = [[id,t]]
        # else:
        #     self.start[stationName].append([id,t])
        if stationName not in self.station_in_out_details:
            self.station_in_out_details[id] = [stationName,t]
        # print("In")
        # print(self.station_in_out_details)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # if stationName not in self.end:
        #     self.end[stationName] = [[id,t]]
        # else:
        #     self.end[stationName].append((id,t))
        co = self.station_in_out_details.get(id)
        self.station_in_out_details.pop(id)
        key = (co[0],stationName)
        
        if key in self.details:
            self.details[key] = (self.details[key][0] + t - co[1], self.details[key][1] + 1)
        else:
            self.details[key] = (t - co[1], 1)
            
        
        # print("Out")
        # print(self.station_in_out_details)
        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        s, n = self.details[key]
        return s / (n * 1.0)
        
        
        
#         total,count = 0,0
        
#         for i in self.start[startStation]:
#             for j in self.end[endStation]:
#                 if i[0] == j[0]:
#                     total = total + (j[1] - i[1])
#                     count = count + 1 
        
#         return (total/count)


            
        
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
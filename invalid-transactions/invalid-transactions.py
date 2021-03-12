class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        for i in range(len(transactions)):
            name1,time1,price1,city1 = transactions[i].split(',') 
            if int(price1) > 1000:
                res.append(transactions[i])
                continue  
            for j in range(len(transactions)):
                if i!=j:
                    name2,time2,price2,city2 = transactions[j].split(',')
                    if name1 == name2 and city1!=city2 and abs(int(time2)-int(time1)) <= 60:
                        res.append(transactions[i])
                        break
         
        return res
        
#         for i, t1 in enumerate(transactions):
#             name1, time1, amount1, city1 = t1.split(',')
#             if int(amount1) > 1000:
#                 invalid.append(t1)
#                 continue
#             for j, t2 in enumerate(transactions):
#                 if i != j: 
#                     name2, time2, amount2, city2 = t2.split(',')
#                     if name1 == name2 and city1 != city2 and abs(int(time1) - int(time2)) <= 60:
#                         invalid.append(t1)
#                         break
        
#         return invalid
                
                    
                    
                    
                    
                    
                    
                
class Solution:
    def minPartitions(self, n: str) -> int:
        dicti = {'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2,'1':1,'0':0}
        for x in dicti:
            if x in n:
                return x
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        temp = []
        for t in time:
            temp.append(t%60)
        
        dicti = {}
        for i in range(len(temp)):
            if temp[i] not in dicti:
                dicti[temp[i]] = 1
            else:
                dicti[temp[i]] += 1
        print(dicti.keys())
        count = 0
        for k in range(0,31):
            if k in dicti.keys():
                if k==0 :
                    count = count + ( dicti[k]*(dicti[k]-1)//2)
                    del dicti[k]
                elif k==30 :
                    
                    count = count +  (dicti[k]*(dicti[k]-1)//2)
                    del dicti[k]
                else:
                    # print(dicti[60-k])
                    count = count + (dicti.get(k,0) *(dicti.get(60-k,0)))
                # print(count)
        # print(dicti)
        return (count)
            
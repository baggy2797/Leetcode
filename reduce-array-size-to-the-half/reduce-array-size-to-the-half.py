class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        
        m = collections.defaultdict(int)
        for v in arr:
            m[v] += 1

        l = []
        for k in m:
            l.append(m[k])

        l.sort(reverse=True)
        cnt = int((len(arr)+1)/2)

        i = 0
        while i<len(l):
            cnt -= l[i]
            if cnt <= 0:
                break
            i += 1
        return i+1
        count_of_numbers = {}
        length = len(arr)
        result = []
        max_length = 0
        for i in range(len(arr)):
            if arr[i] not in count_of_numbers:
                count_of_numbers[arr[i]] = 1
            else:
                count_of_numbers[arr[i]] += 1
                
        # print(count_of_numbers)
        max_length = max(count_of_numbers.values())
        # print(max_length)
        # seen = set()
        
        def findmaximum(count_of_numbers):
            maximum = (-1)*sys.maxsize
            key_maximum = 0
            for key,value in count_of_numbers.items():
                if value > maximum:
                    maximum = value
                    key_maximum = key
            # print(maximum,key_maximum)
            del count_of_numbers[key_maximum]
            return maximum
        
        i = max_length
        count = 0
        rem = 0
        while rem < (length//2) and i >=0:
            maximum = findmaximum(count_of_numbers)
            # print(maximum)
            rem += maximum
            count+=1
            i = i-1
            # print(i)
        return (count)
        
        
            
            
        
            
        
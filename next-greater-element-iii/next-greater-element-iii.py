class Solution:
    def nextGreaterElement(self, n: int) -> int:
        dummy = n
        n = list(str(n))
        
        length = len(n)
        idx =0
        for i in range(len(n)-1,-1,-1):
            if n[i] <= n[i-1]:
                continue
            else:
                idx = i-1
                break
        pivot = 0 
        
        for j in range(idx+1,len(n)):
            
            if n[idx]<n[j]:
                pivot = j
        
        n[pivot],n[idx] = n[idx],n[pivot]
        
        temp = []
        for k in range(len(n)-1,-1,-1):
            if k == idx:
                break
            else:
                temp.append(n[k])
        
        res = n[:idx+1]+temp
        res = "".join(res)
        
        if res <= str(dummy) or int(res)>2147483647: 
            return -1
        return (res)   
            
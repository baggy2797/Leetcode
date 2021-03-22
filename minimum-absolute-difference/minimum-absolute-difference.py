class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        ans=[]
        mini=sys.maxsize
        for i in range(len(arr)-1):
            temp=arr[i+1]-arr[i]
            if temp < mini:
                mini=temp
        for i in range(len(arr)-1):
            temp=abs(arr[i+1]-arr[i])
            if temp==mini:
                ans.append([arr[i],arr[i+1]])
        return ans
                
                
        
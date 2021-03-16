class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        A =arr
        L = len(A)
        n = 0
        
        for i in range(L-2):
            x = A[i]
            for j in range(i+1,L-1):
                y = A[j]
                if abs(x-y) <= a:
                    for k in range(j+1,L):
                        z = A[k]
                        if abs(y-z)<=b and abs(x-z)<=c:
                            n += 1
        return n
        
        # res = []
        # for i in range(len(arr)):
        #     for j in range(0,i):
        #         for k in range(0,j):
        #             if abs(arr[i] - arr[j]) <=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
        #                 temp = []
        #                 temp.append(arr[i])
        #                 temp.append(arr[j])
        #                 temp.append(arr[k])
        #                 res.append(temp)
        # return res
                        
        
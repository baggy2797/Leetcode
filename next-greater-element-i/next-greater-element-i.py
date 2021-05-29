class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashMap = {}
        res = [0 for _ in range(len(nums1))]
        
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                hashMap[stack.pop()] = nums2[i]
            stack.append(nums2[i])
            
        while stack:
            hashMap[stack.pop()] = -1
            
        for i in range(len(nums1)):
            res[i] = hashMap.get(nums1[i])
        
        return res
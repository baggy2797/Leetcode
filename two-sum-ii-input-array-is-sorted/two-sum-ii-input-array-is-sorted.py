class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            search = target - numbers[i]
            if search in numbers:
                if i!=numbers.index(search):
                    return [min(i+1,numbers.index(search)+1),max(i+1,numbers.index(search)+1)]
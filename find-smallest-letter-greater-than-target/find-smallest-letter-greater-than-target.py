class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        for char in letters:
            if char > target:
                return char
        return letters[0]
            
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        while True:
            my_number = randint(low, n + 1)
            if guess(my_number) == 1:
                low = my_number
            elif guess(my_number) == -1:
                n = my_number
            else:
                return my_number
            
        
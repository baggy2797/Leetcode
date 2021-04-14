class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.directory = [0]*maxNumbers
        self.seen = set()
        for i in range(maxNumbers):
            self.seen.add(i)
    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.seen:
            temp = self.seen.pop()
            self.directory[temp]=1
            return temp
        else: return -1
        
    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        if number not in self.seen:return False
        return True
        # pass

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.seen.add(number)
        self.directory[number] = 0


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
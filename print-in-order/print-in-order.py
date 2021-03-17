class Foo:
    def __init__(self):
        
        self.c = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        while self.c != 0:
            continue
        printFirst()
        self.c = 1
            
        
    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while self.c!=1:
            continue
        printSecond()
        self.c = 2
            


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while self.c!=2:
            continue
        printThird()
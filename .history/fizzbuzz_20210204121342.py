# FizzBuzz is when the number is divisible by 3 print fizz when with 5 print buzz and 
# when with both print FizzBuzz



for i in range(1,101):
    c3,c5 = 0,0
    
    d = ""
    c3 = c3+1
    c5 = c5+1
    if c3 == 3:
        d += "fizz"
        c3 = 0
    if c5 == 5:
        d += "buzz"
        c5 = 0
    
    print(d or i)
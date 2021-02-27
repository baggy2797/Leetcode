# FizzBuzz is when the number is divisible by 3 print fizz when with 5 print buzz and 
# when with both print FizzBuzz



for i in range(1,101):
    c3,c5 = 0,0
    
    d = ""
    if c3 == 3:
        d += "fizz"
    if c5 == 5:
        d += "buzz"
    print(d or i)
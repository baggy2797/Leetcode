# FizzBuzz is when the number is divisible by 3 print fizz when with 5 print buzz and 
# when with both print FizzBuzz



for i in range(1,101):
    c3,c5 = 0,0
    
    d = ""
    if i%3 == 0:
        d += "fizz"
    if i%5 == 0:
        d += "buzz"
    print(d or i)